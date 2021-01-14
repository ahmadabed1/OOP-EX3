from EdgeData import EdgeData

class NodeData:
  def __init__(self, key, pos):
    self.id = key
    self.pos = pos
    self.neighbors = {} ## key=int,value=edge_data
    self.in_nodes = list()

  def __repr__(self):
    return '{}: |edges out| {} |edges in| {}'.format(self.id, self.degree(), len(self.in_nodes))

  def get_weight(self, key):
    return self.neighbors[key].get_weight()

  def get_key(self):
    return self.id

  def get_pos(self):
    return self.pos

  def set_in_node(self, other_node):
    self.in_nodes.append(other_node)

  def connect(self, key, other_key, weight):
    if other_key not in self.neighbors.keys():
      self.neighbors[other_key] = EdgeData(key, other_key, weight)

  def remove(self, key):
    return self.neighbors.pop(key) if key in self.neighbors.keys() else None

  def key_NI(self):
    return self.neighbors.keys()

  def edge_NI(self):
    return self.neighbors.values()

  def get_neighbors(self):
    return self.neighbors

  def is_connect(self, key):
    return key in self.neighbors.keys()

  def has_edge(self, key):
    return self.neighbors[key] is not None

  def degree(self):
    return len(self.neighbors.keys())