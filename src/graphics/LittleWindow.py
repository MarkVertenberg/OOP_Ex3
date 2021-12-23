from typing import List

import pygame

from src.graphics.InputBox import InputBox

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (75, 118, 229)
LIGHT_YELLOW = (255, 253, 126)


class LittleWindow:

    def __init__(self, input_boxes: List[InputBox] = None, buttons=None, connected=None):
        self.connected = connected
        self.input_boxes = input_boxes
        self.buttons = buttons
        if connected:
            if self.buttons:
                for button in self.buttons:
                    button.x += self.connected.x
                    button.y += self.connected.y
            if self.input_boxes:
                for input_box in self.input_boxes:
                    input_box.x += self.connected.x
                    input_box.y += self.connected.y

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.connected.is_over(pos):
                self.connected.is_clicked = False
        if self.buttons:
            for button in self.buttons:
                button.handle_event(event)
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.handle_event(event)

    def draw(self, screen, outline):
        if outline:
            pygame.draw.rect(screen, BLACK, self.connected.get_rect(), outline)
        pygame.draw.rect(screen, WHITE, self.connected.get_rect())
        if self.buttons:
            for button in self.buttons:
                button.draw(screen, 4)
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.draw(screen, 4)

    def reset_data(self):
        if self.input_boxes:
            for input_box in self.input_boxes:
                input_box.text = ''
