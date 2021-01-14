from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
import heapq


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, my_graph=None):
        self.my_graph = my_graph

    def get_graph(self):
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            import json
            self.my_graph = DiGraph()
            with open(file_name) as json_file:
                data = json.load(json_file)
                for n in data['Nodes']:
                    self.my_graph.add_node(n['id'])
                for e in data['Edges']:
                    self.my_graph.add_edge(e['src'], e['dest'], e['w'])
        except:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        # try:
        import json
        data = {'Nodes': [], 'Edges': []}
        with open(file_name, 'w+') as f:
            for n in self.my_graph.get_all_v().keys():
                data['Nodes'].append({'id': n})
            for n, n_data in self.my_graph.get_all_v().items():
                for edge in n_data.edge_NI():
                    data['Edges'].append({'src': edge.get_src(), 'dest': edge.get_dest(), 'w': edge.get_weight()})
            f.write(json.dumps(data))
        # except: return False
        return True

    def track_path(self, parent, j, path):
        if parent[j] == -1:
            return
        self.track_path(parent, parent[j], path)
        path.append(j)

    def find_path(self, dist, parent, src, dest):
        for i in range(1, len(dist)):
            if i == dest:
                path = list()
                self.track_path(parent, i, path)
                path.insert(0, src)
                return path

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
        #>>> from GraphAlgo import GraphAlgo
        #>>> g_algo = GraphAlgo()
        #>>> g_algo.addNode(0)
        #>>> g_algo.addNode(1)
        #>>> g_algo.addNode(2)
        #>>> g_algo.addEdge(0,1,1)
        #>>> g_algo.addEdge(1,2,4)
        #>>> g_algo.shortestPath(0,1)
        #(1, [0, 1])
        #>>> g_algo.shortestPath(0,2)
        #(5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        graph = self.my_graph.get_all_v()
        distances = {vertex: float('Infinity') for vertex in graph.keys()}  ## initial all vertices distances to inf.
        distances[id1] = 0  ## the first vertex is defined as distance 0
        parent = [-1] * len(graph.keys())

        pq = [(0, id1)]
        ## expanding all vertices distance by distance to find the optimal path
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue

            for neighbor in graph[current_vertex].key_NI():
                distance = current_distance + graph[current_vertex].get_weight(neighbor)

                ## verify the best path to take
                if distance < distances[neighbor]:
                    parent[neighbor] = current_vertex
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        path = self.find_path(distances, parent, id1, id2)
        ## return the exact shortest path from id1 to id2
        return (distances[id2], path if distances[id2] != float('Infinity') else [])

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        v_set = set()
        sccs = self.connected_components()
        for scc in sccs:
            if id1 in scc:
                for i in scc:
                    v_set.add(i)
        return list(v_set)
        # list = []
        # for node in self.my_graph.get_all_v().values():
        #     if self.shortest_path(id1, node.get_key()) != -1 and self.shortest_path(node.get_key(),id1) :
        #         list.append(node.get_key())
        #
        #     return list

    def connected_components(self):  # -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        # list = [] #this is an eterativ idea
        # for node in self.my_graph.get_all_v().values():
        #     list1=self.connected_component(node.get_key())
        #     list.append(list1)
        # return list

        def Vorder(v, visited, stack, g, gn): #this in a recoratin idea
            visited[v] = True  ## mark current vertex as visited
            ## continue to all this vertex adjacents
            for n in gn.keys():
                if not visited[n]:
                    Vorder(n, visited, stack, g, g[n].get_neighbors())
            stack = stack.append(v)

        def dfs_traversal(v, visited, g, gn, scc):
            visited[v] = True  ## mark current vertex as visited
            scc.append(v)
            ## continue to all this vertex adjacents
            for n in gn.keys():
                if not visited[n]:
                    dfs_traversal(n, visited, g, g[n].get_neighbors(), scc)

        def get_Tgraph(g):
            gr = DiGraph()
            for v, v_data in g.items():
                for e in v_data.edge_NI():
                    gr.add_node(e.get_dest())
                    gr.add_node(e.get_src())
                    gr.add_edge(e.get_dest(), e.get_src(), e.get_weight())
            return gr.get_all_v()

        stack = list()  ## contains the visited vertices
        g = self.my_graph.get_all_v()
        visited = [False] * (len(g.keys()))  ## marking not visited vertices for the DFS

        ## determining the vertices stack by their finishing time
        for node_id in g.keys():
            if not visited[node_id]:
                Vorder(node_id, visited, stack, g, g[node_id].get_neighbors())

        gr = get_Tgraph(g)  ## traspose graph
        visited = [False] * (len(g.keys()))  ## marking not visited vertices for the transpose DFS

        sccs = list()
        ## processing all veritces in the order they defined by the stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = list()
                if i in gr.keys():
                    dfs_traversal(i, visited, gr, gr[i].get_neighbors(), scc)
                else:
                    scc.append(i)
                if len(scc) > 0:
                    sccs.append(scc)
        return sccs

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph().to_directed()
        for n, n_data in self.my_graph.get_all_v().items():
            G.add_node(n, pos=n_data.get_pos())
        for n, n_data in self.my_graph.get_all_v().items():
            for edge in n_data.edge_NI():
                G.add_edge(edge.get_src(), edge.get_dest())

        # print("Nodes of graph: ")
        # print(G.nodes())
        # print("Edges of graph: ")
        # print(G.edges())

        nx.draw(G, with_labels=True)
        # plt.savefig("path/to/some/location/name.png")  # save as png
        plt.show()  # display
