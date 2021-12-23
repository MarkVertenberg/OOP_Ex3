from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def load_from_json(self, file_name: str):
        pass

    def save_to_json(self, file_name: str):
        pass

    def shortest_path(self, id1: int, id2: int):
        pass

    def TSP(self, node_lst: List[int]):
        pass

    def centerPoint(self):
        pass

    def plot_graph(self):
        from GraphGUI import GraphGUI
        gui = GraphGUI(self)
        gui.run_gui()
