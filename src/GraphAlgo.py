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
                        self.graph.add_node(t, (x, y, z))
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
        tip = []

        for e in self.graph.edges:
            List = {}
            src = e[0]
            dest = e[1]
            w = self.graph.edges[e]
            tip.append({"src": src, "dest": dest, "w": w})
        ver = []
        List["Edges"] = ver
        for n in self.graph.nodes.values():
            if n.pos is not None:
                id = n.key
                x = n.pos[0]
                y = n.pos[1]
                z = n.pos[2]
                pos = f'{x},{y},{z}'
                ver.append({"id": id, "pos": pos})
            else:
                ver.append({"id": n.key, "pos": None})
        List["Nodes"] = ver


        return List

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

    def farthest_node_from_src(self, src):
        max = 0
        dis = 0
        for Node in self.graph.nodes:
            dis = self.shortest_path(src, Node)[0]
            if dis > max:
                max = dis
        return max

    def centerPoint(self):
        min = float("inf")
        N = None
        for Node in self.graph.nodes:
            dis = self.farthest_node_from_src(Node)
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
