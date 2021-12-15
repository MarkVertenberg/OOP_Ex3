from typing import List

from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def get_graph(self):
        pass

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
        pass
