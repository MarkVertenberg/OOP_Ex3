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
            with open(str) as f:
                obj = json.load(f)
                list = obj['Edges']
                for i in range(len(list)):
                    self.graph.add_edge(list[i].get("src"), list[i].get("w"), list.get("dest"))

                list1 = obj['Nodes']
                for i in range(len(list)):
                    self.graph.add_node(list1[i].get("id"), list1[i].get("pos"))

                    return True

        except:
            return False

    def save_to_json(self, file_name: str):
        with open(str) as json_file:
            data = json.load(json_file)
            temp = data["Nodes"]
            for Node in self.graph.nodes.values():
                if Node is not None:
                    dist = f'{Node.pos[0]},{Node.pos[1]},{Node.pos[2]}'
                    e = {"id": Node.key, "pos": dist}
                    temp.append(e)
            temp1 = data["Edges"]
            for Edge in self.graph.edges:
                src = f'{Edge[0]}'
                dest = f'{Edge[1]}'
                w = f'{Edge[2]}'
                d = {"src": src, "dest": dest, "w": w}
                temp1.append(d)
        self.writejson(data, file_name)

        pass

    def writejson(data, file_name: str):
        with open(file_name, "w") as f:
            json.dump(data, f)

    def shortest_path(self, id1: int, id2: int):
        try:
            return DIJKSTRA.shortest_path(self.graph, id1, id2)
        except ValueError as e:
            print(e)
        return float('inf'), []

    def TSP(self, node_lst: List[int]):
        sum = 0
        path = []
        iterator = iter(node_lst)
        i = 0
        for n in iterator:
         i = i+1
         if i<2:
            k = next(iterator)
         p = DIJKSTRA.shortest_path_(self.graph, n, k)
         sum = sum + DIJKSTRA.shortest_path_dist(self.graph, n, k)

         path.append(p)



        return path

    #problem in out edges, dosent show the keys of outedges
    def farthest_neighbor_of_node(self, src):
        num = 0
        dist = 0
        visited = [False] * len(self.graph.nodes)
        out_edges = self.graph.all_out_edges_of_node(src)
        for neighbor in out_edges.keys():
            if not visited[neighbor]:
                dist = DIJKSTRA.shortest_path_dist(self.graph, src, neighbor)
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
        gui.run_gui()
