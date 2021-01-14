import unittest
from DiGraph import DiGraph
import time

from src.NodeData import NodeData


class DiGraphtest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        starttime = time.time()

        self.c = DiGraph()  # creates an empty directed graph
        for n in range(5):
            self.c.add_node(n)
        self.c.add_edge(0, 1, 1)
        self.c.add_edge(1, 0, 1.1)
        self.c.add_edge(1, 2, 1.3)
        self.c.add_edge(2, 3, 1.1)
        self.c.add_edge(1, 3, 1.9)
        self.c.remove_edge(1, 3)
        self.c.add_edge(1, 3, 10)
        self.c.add_edge(0, 4, 10)
        self.c.add_edge(4, 0, 10)

        self.d = DiGraph()

        self.g = DiGraph()

        self.g1 = DiGraph()

        self.d.add_node(1)
        self.d.add_node(2)
        self.d.add_node(3)
        self.d.add_edge(1, 2, 3)
        self.d.add_edge(1, 3, 3)
        self.d.add_edge(2, 3, 3)
        for n in range(20):
            self.g.add_node(n)
        self.g1.add_node(1)
        self.g1.add_node(2)
        self.g1.add_node(3)
        self.g1.add_node(4)
        self.g1.add_edge(1, 2, 3)
        self.g1.add_edge(1, 3, 3)
        self.g1.add_edge(1, 4, 3)
        self.g1.add_edge(2, 3, 3)
        self.g1.add_edge(4, 2, 3)

    def test_get_ms(self):
        self.assertEqual(6, self.d.get_mc())

    def test_v_size(self):
        self.assertEqual(20, self.g.v_size())

    def test_e_size(self):
        self.assertEqual(self.d.e_size(), 3)



    def test_add_egde(self):
        self.assertTrue(self.g1.add_edge(3, 4, 2), True)

    def test_add_node(self):
        self.assertTrue(self.g1.add_node(30), True)

    def test_remove_node(self):
        self.assertTrue(self.g1.remove_node(2), True)

    def test_remove_edge(self):
        self.assertTrue(self.g1.remove_edge(1, 2),True)

    def test_all_in_edge_of_node(self):
        self.assertEqual(self.c.all_in_edges_of_node(1), {0: 1})

    def test_all_out_of_node(self):
        self.assertEqual(self.c.all_out_edges_of_node(1),{0: 1.1, 2: 1.3, 3: 10})






# toto = {1: tuple(NodeData(1)), 2: tuple(NodeData(2)), 3:tuple( NodeData(3)), 4:tuple( NodeData(4))}
# toto = {1:(1, NodeData(1)), 2: (2, NodeData(2)), 3: (3, NodeData(3)), 4:(4, NodeData(4))}
# self.my_graph[node_id] = NodeData(node_id, pos)
# test=dict()
# test.update(toto)
# test[1]=NodeData(1)
# test[2]=NodeData(2)

# test[2]=NodeData(2)
# test[3]=NodeData(3)
# test[4]=NodeData(4)
# print(test)

# check=dict(1=NodeData(1),2=NodeData(2))

# print(self.g1.get_all_v())
# print(type(test[1]))
# for x in self.g1.get_all_v().items():
#     print(x)
#     print(type(x))
# print(self.g1.get_all_v()[[1]])
# if type(test) == type(self.g1.get_all_v()):
#  print('equal')
# print(len(toto))
# print(len(self.g1.get_all_v()))
# print(type(self.g1.get_all_v()))
# print(dict(toto))
# print(dict(self.g1.get_all_v()))
# if ( dict(toto) == dict(self.g1.get_all_v())):
#    print('yes')
# else:
#     print(toto)
# if ( toto is self.g1.get_all_v()):
#     print('yes')
# self.assertDictEqual({0: NodeData(0), 1: NodeData(1), 2: NodeData(2), 3: NodeData(3), 4: NodeData(4)}, self.c.get_all_v())


if __name__ == '__main__':
    unittest.main(verbosity=True)
