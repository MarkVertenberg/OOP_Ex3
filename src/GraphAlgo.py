import queue
from typing import List
import json
import random

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from Dijkstra import Dijkstra
from src.DiGraph import DiGraph

DIJKSTRA = Dijkstra()


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph
        self.mc = 0
        self.list = [int]

    def get_graph(self):
        return self.graph

    def load_from_json(self, file_name: str):
        try:
            self.graph = DiGraph()
            with open(file_name, "r") as fp:
                obj = json.load(fp)
                for n in obj["Nodes"]:
                    t = int(n["id"])
                    if "pos" in n:
                        m = n["pos"].split(',')
                        x = float(m[0])
                        y = float(m[1])
                        z = float(m[2])
                        self.graph.add_node(t, x, y, z)
                    else:
                        self.graph.add_node(t)
                for e in obj["Edges"]:
                    src = int(e["src"])
                    dest = int(e["dest"])
                    w = float(e["w"])
                    self.graph.add_edge(src, dest, w)
        except:
            return False

        return True


    def save_to_json(self, file_name: str):
        try:
            file = open(file_name, 'w')
            file.write(json.dumps(self.savefile()))
            file.close()
            return True
        except IOError:
            return False


    def savefile(self):
        Edges = []
        for e in self.graph.edges:
            src = e[0]
            dest = e[1]
            w = self.graph.edges[e]
            Edges.append({"src": src, "dest": dest, "w": w})
            Nodes = []
        for n in self.graph.nodes.values():
            if n.pos is not None:
                id = n.key
                pos = f'{n.pos[0]},{n.pos[1]},{n.pos[2]}'
                Nodes.append({"id": id, "pos": pos})
            else:
                Nodes.append({"id": n.key, "pos": None})
                list = {}
        list["Edges"] = Edges
        list["Nodes"] = Nodes
        return list


    def shortest_path(self, id1: int, id2: int):
        try:
            return DIJKSTRA.shortest_path(self.graph, id1, id2)
        except ValueError as e:
            print(e)
        return float('inf'), []

    def TSP(self, node_lst: List[int]):
        sum = 0
        path = []
        if len(node_lst) > 0:
            path.append(node_lst[0])
            src = node_lst[0]
            for node in node_lst[1:]:
                algo = self.shortest_path(src, node)  # (dist, list(nodes))
                pa = algo[1]
                sum += algo[0]
                src = node
                for p in pa[1:]:
                    path.append(p)
        return path, sum

    #problem in out edges, dosent show the keys of outedges
    def farthest_neighbor_of_node(self, src):
        num = 0
        dist = 0
        visited = [False] * len(self.graph.nodes)
        out_edges = self.graph.all_out_edges_of_node(src)
        for neighbor in out_edges.keys():
            if not visited[neighbor]:
                dist = self.shortest_path(src, neighbor)[0]
                visited[neighbor] = True
                if num < dist:
                    num = dist
        return dist

    def centerPoint(self):
        min = float("inf")
        N = None
        for Node in self.graph.nodes:
          dis = self.farthest_neighbor_of_node(Node)
          if dis < min:
            min = dis
            N = Node
        return N, min

    def plot_graph(self):
        from GraphGUI import GraphGUI
        gui = GraphGUI(self)
        for node in self.graph.get_all_v().values():
            if not node.get_y() and not node.get_x():
                node.x = random.randint(0, gui.WIDTH)
                node.y = random.randint(0, gui.HEIGHT)
        gui.plot_graph()
