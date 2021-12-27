from typing import List

import pygame

from src.graphics.InputBox import InputBox
from src.graphics.Text import Text

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (75, 118, 229)
LIGHT_YELLOW = (255, 253, 126)


class LittleWindow:

    def __init__(self, input_boxes: List[InputBox] = None, button=None, related=None, function=None):
        self.related = related
        self.input_boxes = input_boxes
        self.button = button
        self.massage = Text(160, 60, "Text")
        self.function = function
        if related:
            if self.button:
                self.button.x += self.related.x
                self.button.y += self.related.y
            if self.input_boxes:
                for input_box in self.input_boxes:
                    input_box.x += self.related.x
                    input_box.y += self.related.y
            self.massage.x += self.related.x
            self.massage.y += self.related.y

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.related.is_over(pos):
                self.related.is_clicked = False
        if self.button:
            self.button.handle_event(event)
            if self.button.is_clicked:
                self.massage.text = "button Clicked"
                # self.function()
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.handle_event(event)

    def draw(self, screen, outline):
        if outline:
            pygame.draw.rect(screen, BLACK, self.related.get_rect(), outline)
        print(self.massage.text)
        if self.massage.text != '':
            print("passed")
            self.massage.draw(screen)
        if self.button:
            self.button.draw(screen, 2)
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.draw(screen, 2)

    def reset_data(self):
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.text.text = ''
        self.massage.text = ''
