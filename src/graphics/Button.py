import pygame

from src.graphics.LittleWindow import LittleWindow

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (75, 118, 229)
LIGHT_YELLOW = (255, 253, 126)


class Button:
    """
        Class that representing a button in pygame.
    """

    def __init__(self, color, x, y, width, height, text='', text_color=BLACK, text_size=48, window=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.is_clicked = False
        self.window = window
        if window:
            self.window = LittleWindow(window.input_boxes, window.buttons, self)

    def handle_event(self, event, over_color=SKY_BLUE, not_over_color=WHITE, over_color_text=WHITE, not_over_color_text=BLACK):
        pos = pygame.mouse.get_pos()
        if self.is_clicked and self.window:
            self.window.handle_event(event)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_over(pos):
                    print(self.text + " button is clicked!")
                    self.is_clicked = True
                    if self.window:
                        self.window.reset_data()
                else:
                    self.is_clicked = False
            if event.type == pygame.MOUSEMOTION:
                if self.is_over(pos):
                    self.text_color = over_color_text
                    self.color = over_color
                else:
                    self.text_color = not_over_color_text
                    self.color = not_over_color

    def draw(self, screen, outline=None):
        """ draw the button on the screen """
        if self.window and self.is_clicked:
            self.window.draw(screen, outline)
        else:
            if outline:
                pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), outline)
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

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

    def get_rect(self):
        return self.x, self.y, self.width, self.height
