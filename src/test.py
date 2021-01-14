from DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData
import time
import matplotlib.pyplot as plt
from abc import ABC

aaa=DiGraph()
aaa.add_node(1)
aaa.add_node(2)
aaa.add_node(3)
aaa.add_edge(1, 2, 3)
aaa.add_edge(1, 3, 3)
aaa.add_edge(2, 3, 3)


z=GraphAlgo()
z.my_graph=DiGraph()
z.my_graph.add_node(1)
z.my_graph.add_node(2)
z.my_graph.add_node(3)
z.my_graph.add_node(4)
z.my_graph.add_edge(1, 2, 9)
z.my_graph.add_edge(1, 3, 1)
z.my_graph.add_edge(2, 3, 1)
z.my_graph.add_edge(3, 2, 1)
z.my_graph.add_edge(1, 4, 1)
z.my_graph.add_edge(4, 2, 1)

#print(z.shortest_path(2,3))

c = DiGraph()  # creates an empty directed graph
for n in range(5):
        c.add_node(n)
        c.add_edge(0, 1, 1)
        c.add_edge(1, 0, 1.1)
        c.add_edge(1, 2, 1.3)
        c.add_edge(2, 3, 1.1)
        c.add_edge(1, 3, 1.9)
        c.remove_edge(1, 3)
        c.add_edge(1, 3, 10)
        c.add_edge(0, 4, 10)
        c.add_edge(4, 0, 10)
print(c.all_out_edges_of_node(1))

g = DiGraph()  # creates an empty directed graph
for n in range(5):
        g.add_node(n)
g.add_edge(0, 1, 1)
g.add_edge(1, 0, 1.1)
g.add_edge(1, 2, 1.3)
g.add_edge(2, 3, 1.1)
g.add_edge(3, 4, 0.8)
g.add_edge(1, 3, 1.9)
g.remove_edge(1, 3)
g.add_edge(1, 3, 10)
g.add_edge(0, 4, 10)
g.add_edge(4, 0, 10)

g2 = DiGraph()
g2.add_edge(0, 1, 1)
g2.add_edge(1, 0, 1.1)
g2.add_edge(1, 2, 1.3)
g2.add_edge(2, 3, 1.1)
g2.add_edge(1, 3, 1.9)
g2.add_edge(1, 3, 10)
g2.add_edge(0, 4, 10)
g2.add_edge(4, 0, 10)
g_algo = GraphAlgo(g2)

#print(g_algo.shortest_path(1,3))
#print(g)  # prints the __repr__ (func output)
#print(g.get_all_v())  # prints a dict with all the graph's vertices.
#print(g.all_in_edges_of_node(1))
#print(g.all_out_edges_of_node(1))
g_algo = GraphAlgo(g)
#print(z.shortest_path(1, 2))
#print(g_algo.connected_components())
#print(g_algo.connected_component(0))
#print(g_algo.get_graph())
#print(g)
#g2 = DiGraph()
#g=GraphAlgo(g2)
#g.save_to_json("test_graph_obj")
#g4=GraphAlgo().load_from_json("test_graph_obj")
#print(g4)
#print(g)
ahmad = GraphAlgo()
file = "../data/G_1000_8000_1.json"
#ahmad.load_from_json(file)
tic=time.perf_counter()
#print(ahmad.connected_component(1))
#print(ahmad.shortest_path(1,5))
#print(ahmad.connected_components())
#print(ahmad.connected_component(1))
#ahmad.plot_graph()
toc=time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
#print(z.shortest_path(1,2))



