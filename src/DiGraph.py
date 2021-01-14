from GraphInterface import GraphInterface
from EdgeData import EdgeData
from NodeData import NodeData


class DiGraph(GraphInterface):
  def __init__(self):
    self.mc = 0
    self.e_num = 0
    self.my_graph = {}

  def __repr__(self):
    return 'Graph: |V|={} , |E|={}'.format(self.v_size(), self.e_size())

  def v_size(self) -> int:
    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """
    return len(self.my_graph.keys())

  def e_size(self) -> int:
    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """
    return self.e_num

  def get_all_v(self) -> dict:
    """
    return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
    """
    return self.my_graph

  def all_in_edges_of_node(self, id1: int) -> dict:
    """return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (key, weight)
     """
    result = {}
    for node_id, node_data in self.my_graph.items():
      for edge in node_data.edge_NI():
        if edge.get_dest() == id1:
          result[node_id] = edge.get_weight()
    return result


  def all_out_edges_of_node(self, id1: int) -> dict:
    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
    weight)
    """
    if id1 in self.my_graph.keys():
      pairs = {}
      for edge in self.my_graph[id1].edge_NI():
        pairs[edge.get_dest()] = edge.get_weight()
      return pairs
    return None


  def get_mc(self) -> int:
    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """
    return self.mc

  def add_edge(self, id1: int, id2: int, weight: float) -> bool:
    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """
    if id1 not in self.my_graph.keys() or id2 not in self.my_graph.keys():
      return
    if id2 not in self.my_graph[id1].key_NI():
      self.my_graph[id1].connect(id1, id2, weight)
      self.my_graph[id2].set_in_node(id1)
      self.e_num += 1
      self.mc += 1
      return True


  def add_node(self, node_id: int, pos: tuple = None) -> bool:
    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    Note: if the node id already exists the node will not be added
    """
    if node_id not in self.my_graph.keys():
      self.my_graph[node_id] = NodeData(node_id, pos)
      self.mc += 1
      return True

  def remove_node(self, node_id: int) -> bool:
    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    Note: if the node id does not exists the function will do nothing
    """
    if node_id in self.my_graph.keys():
      edges = self.my_graph[node_id].edge_NI()
      for edge in self.my_graph[node_id].edge_NI():
        del edge
      node_data = self.my_graph.pop(node_id)
      del node_data
      self.mc += 1
      return True
    return False

  def remove_edge(self, node_id1: int, node_id2: int) -> bool:
    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.
    Note: If such an edge does not exists the function will do nothing
    """
    if node_id1 in self.my_graph.keys():
      for edge in self.my_graph[node_id1].edge_NI():
        if edge.get_src() == node_id1 and edge.get_dest() == node_id2:
          edge_data = self.my_graph[node_id1].remove(edge.get_dest())
          del edge_data
          self.e_num -= 1
          self.mc += 1
          break
          return True
    return False
