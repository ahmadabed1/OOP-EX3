# OOP - Ex3
## This project has been developed as an assignment in OOP course.

In this project we build a dircted weighted graph in PYTHON. \
This project is build by two classes: 
1. `class of graph.`
2. `class of algorithm graph.`
We use our codes that we build in OOP-EX2(in java) and "Translate" the code to Python language, after that we start to compare our results in the two projects (Ex2-JAVA and Ex3-Python).And also compare our results to NetworkX libraries(forbidden to use libraries that is built in Python).

## First Part: 
`The graph class`: \
We bulit this class by `GraphInterface` and it spilted into three part(classes):
1. `NodeData`: This class has these functions init , rept, get_weight, get_key, get_pos, connect, remove, key_NI, edge_NI, get_neighbors, is_conncet, has_edge, degree, get_tag , it returns all about the node data like tag,neighbours,,. 
2. `EdgeData` : This class has these function init , repr, get_src, get_dest, get_weight, it returns the weight of the edge between the src and the dest (src is the start node , and dest is the end node )
3. `DiGraph` : This class has these functions init, repr, v_size, e_size, get_all_v, all_in_edges_of_node, all_out_edges_of_node, get_mc, add_edge, add_node, remove_node, remove_edge, it returns the graph its self , in that we can remove edges between nodes , add edges, add a node to graph and more.
At the end we check ourself by using the check0 that is already built for us , also we bulit a class test `Test_DiGraph`

## Secound Part: 
`Algorithm Graph Class `: \
We bulit this class by `GraphAlgoInterface`, It contains only one class `GraphAlgo` , it has these functions *init, get_graph, load_from_json, save_to_json, shortest_path, connected_component, connected_components, plot_graph * 
1. `init` : init to the graph to use the methods on graphAlgo
2. `get_graph` : it returns the dictionary (key, NodeData)
3. `load_from_json` : load graph from json file (Nodes, Edges)
4. `save_to_json` : save graph from json file (Nodes, Edges)
5. `shortest_path` : find the shortest path between two nodes(src and dest) by using BFS algorithms. For more information:  https://en.wikipedia.org/wiki/Depth-first_search
6. `connected_component` : to find the strongly connected component (SCC) that this node is part of.
7. `connected_components` : finds **all** the strongly connected component (SCC) in the graph.
![toposcc2](https://user-images.githubusercontent.com/73169815/104426361-83cc8a80-558a-11eb-8606-dda1bfc814f0.gif)
8. `plot_graph` : to plots the graph. If the nodes have a position, the nodes will be placed there.Otherwise, they will be placed in a random but elegant manner.
