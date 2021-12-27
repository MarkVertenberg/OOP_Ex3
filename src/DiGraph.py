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
        return self.nodes[id1].inWard

    def all_out_edges_of_node(self, id1: int):
        return self.nodes[id1].outWard

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
      if id1 in self.nodes and id2 in self.nodes:
        self.edges[(id1, id2)] = weight
        self.nodes[id1].outWard[id2] = weight
        self.nodes[id2].inWard[id1] = weight
        self.mc = self.mc + 1
        return True
      else:
          return False

    def add_node(self, node_id: int, pos: tuple = None):
        if self.nodes.get(node_id) is None:
            self.nodes[node_id] = Node(node_id, pos)
            self.mc = self.mc + 1
            return True
        else:
            return False

    def remove_node(self, node_id: int):
        if self.nodes[node_id] is not None:
            self.nodes.pop(node_id)
            self.mc = self.mc + 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 in self.nodes[node_id2].inWard and node_id2 in self.nodes[node_id1].outWard:
            self.nodes[node_id1].outWard.pop(node_id2)
            self.nodes[node_id2].inWard.pop(node_id1)
            self.mc += 1
            return True
        return False


class Node:
    def __init__(self, key, pos: tuple = None):
        from src.graphics.NodePainter import NodePainter
        self.key = key
        self.outWard = {}
        self.inWard = {}
        self.x = None
        self.y = None
        if pos:
            self.x = pos[0]
            self.y = pos[1]
        self.painter = NodePainter(self)

    def get_key(self):
        return self.key

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        x = math.pow((other.get_x() - self.x), 2)
        y = math.pow((other.get_y() - self.y), 2)
        return math.sqrt(x + y)
