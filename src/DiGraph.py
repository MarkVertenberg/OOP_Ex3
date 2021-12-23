import math

import pygame

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        return len(self.edges)

    def get_all_v(self):
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        return self.nodes[id1].inEdges

    def all_out_edges_of_node(self, id1: int):
        return self.nodes[id1].outEdges

    def get_mc(self):
        pass

    def add_edge(self, id1: int, id2: int, weight: float):
        pass

    def add_node(self, node_id: int, pos: tuple = None):
        pass

    def remove_node(self, node_id: int):
        pass

    def remove_edge(self, node_id1: int, node_id2: int):
        pass


BLACK = (0, 0, 0)
LIGHT_YELLOW = (255, 253, 126)


class Node:
    def __init__(self, key, x, y, color=LIGHT_YELLOW, radius=20):
        self.key = key
        self.x = x
        self.y = y
        self.outEdges = {}
        self.inEdges = {}
        self.color = color
        self.radius = radius

    def get_key(self):
        return self.key

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        x = math.pow((other.getx() - self.x), 2)
        y = math.pow((other.gety() - self.y), 2)
        return math.sqrt(x + y)

    def draw(self, screen, start_x, start_y, pixel_x, pixel_y, min_rage, outline=3):
        pygame.draw.circle(screen, BLACK, (((self.x - min_rage) / pixel_x) + start_x, ((self.y - min_rage) / pixel_y) + start_y), self.radius + outline)
        pygame.draw.circle(screen, self.color, (((self.x - min_rage) / pixel_x) + start_x, ((self.y - min_rage) / pixel_y) + start_y), self.radius)
        font = pygame.font.SysFont('comicsans', 16)
        text = font.render(str(self.key), True, BLACK)
        screen.blit(text, (((self.x - min_rage) / pixel_x) + start_x - text.get_width() / 2, ((self.y - min_rage) / pixel_y) + start_y - text.get_height() / 2))
