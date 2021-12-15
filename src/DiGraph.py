from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def v_size(self):
        pass

    def e_size(self):
        pass

    def get_all_v(self):
        pass

    def all_in_edges_of_node(self, id1: int):
        pass

    def all_out_edges_of_node(self, id1: int):
        pass

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
