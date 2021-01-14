import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class Another_Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.ahmad = GraphAlgo()
        file = "../data/G_20000_160000_1.json.json"
        self.ahmad.load_from_json(file)



    def test_shortest_path(self):
        self.assertEqual(self.ahmad.shortest_path(1, 5), (42.76824927106041, [1, 5]))

    def test_conected_componints(self):
        self.assertEqual(self.ahmad.connected_components(),[[0, 2, 1, 4, 3, 5, 7, 6, 8, 9]])

    def test_Connected_Component(self):
        self.assertEqual(self.ahmad.connected_component(1),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main(verbosity=True)
