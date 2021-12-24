import queue
from typing import List
import json

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from src import Dijkstra


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
        pass

    def shortest_path(self, id1: int, id2: int):

     return Dijkstra.shortest_path(self.graph, id1, id2)


    def TSP(self, node_lst: List[int]):
        pass

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
        for Node in self.graph:
         dis =  self.bfs(self.graph, Node)
         if dis < min:
             min = dis
        #need to return the node not the int?
        return min

    def plot_graph(self):
        from GraphGUI import GraphGUI
        gui = GraphGUI(self)
        gui.run_gui()
