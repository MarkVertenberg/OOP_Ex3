import pygame


class Button:

    BLACK = (0, 0, 0)

    def __init__(self, color, x, y, width, height, text='', text_color=BLACK, text_size=48):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

    def draw(self, screen, outline=None):
        """ draw the button on the screen """
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.text_size)
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        """ Pos is the mouse position or a tuple of (x,y) coordinates,
            returns if the pos is over this button """
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
