import queue
import random
from typing import List
import json

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from src import Dijkstra

DIJKSTRA = Dijkstra()


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None,node:int=None ,edge:int=None,weight:int=None):
        self.graph = graph
        self.node = node
        self.edge = edge
        self.weight = weight

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
        list = []
        for i in node_lst:
            n = self.bfs(self.graph, i)
            list.append(n)
        return list,

        pass

    def return_neighbor(self, s):
        visited = [False] * len(self.graph)
        q = queue.Queue
        q.put(s)
        min = float('inf')
        visited[s] = True

        while not q.empty():
            vert = q.get()
            sum = 0
            Neigh = None
            for neighbor in self.graph[vert]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dis = Dijkstra.shortest_path_dist(self.graph, s, neighbor)
                    if dis < min:
                        min = dis
                        sum = sum + min
                        Neigh = neighbor

        return Neigh, sum

    def add_neighbor(self, src, dest):
        self.graph.nodes[src].append(dest)

    def bfs(self, s):
        visited = [False] * len(self.graph)
        q = queue.Queue
        q.put(s)
        min = float('inf')
        visited[s] = True

        while not q.empty():
            vert = q.get()
            for neighbor in self.graph[vert]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dis = Dijkstra.shortest_path_dist(self.graph, s, neighbor)
                    if dis < min:
                        min = dis
        return min

    def centerPoint(self):
        min = float('inf')
        Center = None
        for Node in self.graph:
            dis = self.bfs(self.graph, Node)
            if dis < min:
                min = dis
                Center = Node

        return Center

    def plot_graph(self):
        from GraphGUI import GraphGUI
        gui = GraphGUI(self)
        for node in self.graph.get_all_v().values():
            if not node.get_y() and not node.get_x():
                node.x = random.randint(0, gui.WIDTH)
                node.y = random.randint(0, gui.HEIGHT)
        gui.run_gui()
