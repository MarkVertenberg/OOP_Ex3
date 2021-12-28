import unittest
from DiGraph import Node
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_Node(self):
        node1 = Node(1, (1.0, 2.0))
        node2 = Node(2, (1.0, 8.0))
        self.assertEqual(1, node1.get_key())
        self.assertEqual(2, node2.get_key())
        self.assertEqual(1.0, node1.get_x())
        self.assertEqual(1.0, node2.get_x())
        self.assertEqual(2.0, node1.get_y())
        self.assertEqual(8.0, node2.get_y())
        self.assertEqual(6.0, node1.distance(node2))

    def test_DiGraph(self):
        test_graph = GraphAlgo()
        test_graph.load_from_json('../data/A0.json')
        self.assertEqual(test_graph.graph.v_size(), 11)
        self.assertEqual(test_graph.graph.e_size(), 22)
        self.assertEqual(len(test_graph.graph.get_all_v()), 11)
        self.assertEqual(len(test_graph.graph.all_in_edges_of_node(0)), 2)
        self.assertEqual(len(test_graph.graph.all_out_edges_of_node(0)), 2)
        test_graph.graph.add_edge(0, 2, 3)
        self.assertEqual(test_graph.graph.Lines[(0, 2)], 3)
        self.assertEqual(test_graph.graph.get_mc(), 34)
        test_graph.graph.add_node(18, (35.21310882485876, 32.104636394957986, 0.0))
        self.assertEqual(test_graph.graph.v_size(), 12)
        self.assertEqual(True, test_graph.graph.remove_node(18))
        self.assertEqual(True, test_graph.graph.remove_edge(0, 1))
        self.assertEqual(False, test_graph.graph.remove_edge(0, 1))

    def test_GraphAlgo(self):
        test_graph = GraphAlgo()
        self.assertTrue(test_graph.load_from_json('../data/A0.json'))
        self.assertTrue(test_graph.save_to_json("saved_file.json"))
        test_graph2 = GraphAlgo()
        test_graph2.graph.add_node(0)
        test_graph2.graph.add_node(1)
        test_graph2.graph.add_node(2)
        test_graph2.graph.add_edge(0, 1, 2)
        test_graph2.graph.add_edge(1, 2, 3)
        self.assertEqual(test_graph2.shortest_path(0, 1), (2, [0, 1]))
        self.assertEqual(test_graph2.shortest_path(0, 2), (5, [0, 1, 2]))
        test_graph2.graph.remove_node(1)
        self.assertEqual(test_graph2.shortest_path(0, 2), (float('inf'), []))
        self.assertEqual(test_graph.centerPoint(), (7, 6.806805834715163))
        path = [1, 4, 7, 3, 6]
        expected = ([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 4, 5, 6], 19.012874172166818)
        self.assertEqual(expected, test_graph.TSP(path))

    """def test_shortestPath(self):
        test_graph = GraphAlgo()
        file = '../bigGraphs/graph100000.json'
        test_graph.load_from_json(file)
        self.assertEqual(test_graph.shortest_path(0, 1), (float("inf"), []))

    def test_tsp(self):
        test_graph = GraphAlgo()
        file = '../bigGraphs/graph100000.json'
        test_graph.load_from_json(file)
        path = [1, 2, 3]
        expected = ([1], float("inf"))
        self.assertEqual(expected, test_graph.TSP(path))

    def test_center(self):
        test_graph = GraphAlgo()
        file = '../bigGraphs/graph1000000.json'
        test_graph.load_from_json(file)
        self.assertEqual(test_graph.centerPoint(), (7, 6.806805834715163))
    """


if __name__ == '__main__':
    unittest.main()
