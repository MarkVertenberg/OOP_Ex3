import math

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
        return self.nodes[id1].In

    def all_out_edges_of_node(self, id1: int):
        return self.nodes[id1].out

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        while True:
          if self.nodes[id1] is None | self.nodes[id2] is None:
                return False



    def add_node(self, node_id: int, pos: tuple = None):
        pass

    def remove_node(self, node_id: int):
        pass

    def remove_edge(self, node_id1: int, node_id2: int):
        pass

    class Node:
        def __init__(self, key, x, y):
            self.key = key
            self.x = x
            self.y = y
            self.out = {}
            self.In = {}

        def Key(self):
            return self.key

        def x(self):
            return self.x

        def y(self):
            return self.y

        def distance(self, g):
            x = math.pow((g.getx() - self.getx()), 2)
            y = math.pow((g.gety() - self.gety()), 2)
            return math.sqrt(x + y)

