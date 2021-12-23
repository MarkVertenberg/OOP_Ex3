import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (75, 118, 229)


class InputBox:
    """
        Class that representing input box in pygame.
    """

    def __init__(self, x, y, width, height, massage='', text='', color=WHITE, color_outline=BLACK, text_size=16, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.massage = massage
        self.text = text
        self.color = color
        self.color_outline = color_outline
        self.text_size = text_size
        self.text_color = text_color
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.is_over(pos):
                self.active = True
                self.color_outline = SKY_BLUE
            else:
                self.active = False
                self.color_outline = BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, self.color_outline, (self.x, self.y, self.width, self.height), outline)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.text_size)
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + 5, self.y + 5))
        elif not self.active:
            font = pygame.font.SysFont('comicsans', self.text_size)
            text = font.render(self.massage, True, self.text_color)
            screen.blit(text, (self.x + 5, self.y + 5))

    def is_over(self, pos):
        """ Pos is the mouse position or a tuple of (x,y) coordinates,
            returns if the pos is over this input box """
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
