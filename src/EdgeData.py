
class EdgeData(object):
  def __init__(self, src, dest, weight):
    self.src = src
    self.dest = dest
    self.weight = weight

  def __repr__(self):
    return '{}->(W={}){}'.format(self.src, self.weight, self.dest)

  def get_src(self):
    return self.src

  def get_dest(self):
    return self.dest

  def get_weight(self):
    return self.weight