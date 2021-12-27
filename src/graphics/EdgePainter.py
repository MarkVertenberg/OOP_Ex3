import math

import pygame.draw

from src.graphics.NodePainter import NodePainter
from src.graphics.Text import Text

BLACK = (0, 0, 0)


class EdgePainter:

    def __init__(self, src: NodePainter, dest: NodePainter, weight, color=BLACK):
        self.src = src
        self.dest = dest
        self.start_x, self.start_y, self.stop_x, self.stop_y = self.start_pos()
        self.color = color
        self.text = None
        self.weight = weight
        self.over = False

    def start_pos(self):
        if self.dest.new_x and self.dest.new_y:
            dx = self.dest.new_x - self.src.new_x
            dy = self.dest.new_y - self.src.new_y
            a = math.atan(abs(dy / dx))
            print(a)
            s_h = math.sin(a) * self.src.radius
            s_w = math.cos(a) * self.src.radius
            d_h = math.sin(a) * self.dest.radius
            d_w = math.cos(a) * self.dest.radius
            if dx >= 0 and dy >= 0:
                return self.src.new_x + s_w, self.src.new_y + s_h, self.dest.new_x - d_w, self.dest.new_y - d_h
            if dx > 0 and dy < 0:
                return self.src.new_x + s_w, self.src.new_y - s_h, self.dest.new_x - d_w, self.dest.new_y + d_h
            if dx < 0 and dy > 0:
                return self.src.new_x - s_w, self.src.new_y + s_h, self.dest.new_x + d_w, self.dest.new_y - d_h
            else:
                return self.src.new_x - s_w, self.src.new_y - s_h, self.dest.new_x + d_w, self.dest.new_y + d_h
        return None, None, None, None

    def draw(self, screen, outline=2):
        self.start_x, self.start_y, self.stop_x, self.stop_y = self.start_pos()
        if self.start_x:
            pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.stop_x, self.stop_y), outline)


