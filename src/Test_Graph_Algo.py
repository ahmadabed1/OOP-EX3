import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class Test_Graph_Algo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.g2 = DiGraph()  # creates an empty directed graph
        for n in range(5):
            self.g2.add_node(n)
        self.g2.add_edge(0, 1, 1)
        self.g2.add_edge(1, 0, 1.1)
        self.g2.add_edge(1, 2, 1.3)
        self.g2.add_edge(2, 3, 1.1)
        self.g2.add_edge(1, 3, 1.9)
        self.g2.remove_edge(1, 3)
        self.g2.add_edge(1, 3, 10)
        self.g2.add_edge(0, 4, 10)
        self.g2.add_edge(4, 0, 10)
        self.g_algo = GraphAlgo(self.g2)
        self.aaa = DiGraph()
        self.aaa.add_node(1)
        self.aaa.add_node(2)
        self.aaa.add_node(3)
        self.aaa.add_edge(1, 2, 3)
        self.aaa.add_edge(1, 3, 3)
        self.aaa.add_edge(2, 3, 3)
        self.z = GraphAlgo()
        self.z.my_graph = DiGraph()
        self.z.my_graph.add_node(1)
        self.z.my_graph.add_node(2)
        self.z.my_graph.add_node(3)
        self.z.my_graph.add_node(4)
        self.z.my_graph.add_edge(1, 2, 9)
        self.z.my_graph.add_edge(1, 3, 1)
        self.z.my_graph.add_edge(2, 3, 1)
        self.z.my_graph.add_edge(3, 2, 1)
        self.z.my_graph.add_edge(1, 4, 1)
        self.z.my_graph.add_edge(4, 2, 1)



    def test_Shortest_Path(self):
        self.assertEqual(self.z.shortest_path(2, 3), (1, [2, 3]))

    def test_Connected_Components(self):
        self.assertEqual(self.g_algo.connected_components(), [[0, 1, 4], [2], [3]])

    def test_Connected_Component(self):
        self.assertEqual(self.g_algo.connected_component(0), [0, 1, 4])

    def test_Get_Graph(self):
        self.assertEqual(self.g_algo.get_graph(),self.g2)

    def test_save_load(self):
        g2 = DiGraph()
        g=GraphAlgo(g2)
        g.save_to_json("test_graph_obj")
        g4=GraphAlgo().load_from_json("test_graph_obj")
        g4.__eq__(g)



