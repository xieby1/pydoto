from pydot import Dot, Edge, Node, Graph, Cluster
from typing import TypeVar
T = TypeVar("T")

def safe_set(args: dict, key: str, value):
  if key not in args: args[key] = value

# Compound Dot
class CDot(Dot):
  def __init__(self, *vargs, **args):
    args["compound"] = True # make the cluster connectable
    safe_set(args, "bgcolor", "transparent")
    Dot.__init__(self, *vargs, **args)
    self.set_node_defaults(shape="box")

# Connectable Cluster
class CCluster(Cluster):
  def __init__(self, name, **args):
    safe_set(args, "label", name)
    Cluster.__init__(self, name, **args)
    self._connect_node_ = addNode(
      self, "_connect_node_", label="", shape="none", width=0, height=0, margin=0)

def addNode(g: Graph|CCluster, name, **args):
  safe_set(args, "label", name)
  n = Node(g.get_name()+name, **args)
  g.add_node(n)
  return n

def addEdge(g: Graph, n1: Node|CCluster, n2: Node|CCluster, **args):
  # auto edge color
  if isinstance(n1, Node)  and n1.get("color"):    safe_set(args, "color", n1.get("color"))
  if isinstance(n1, Graph) and n1.get("pencolor"): safe_set(args, "color", n1.get("pencolor"))
  # auto edge width
  if n1.get("penwidth"): safe_set(args, "penwidth", n1.get("penwidth"))
  if isinstance(n1, CCluster): l = n1._connect_node_; args["ltail"] = n1.get_name()
  else: l = n1
  if isinstance(n2, CCluster): r = n2._connect_node_; args["lhead"] = n2.get_name()
  else: r = n2
  g.add_edge(Edge(l.get_name(), r.get_name(), **args))

def addCCluster(g: Graph|CCluster, name, **args):
  s=CCluster(name, **args)
  g.add_subgraph(s)
  return s

def add(g: Graph, item: T) -> T:
  if   isinstance(item, Node):     g.add_node(item)
  elif isinstance(item, Edge):     g.add_edge(item)
  elif isinstance(item, CCluster): g.add_subgraph(item)
  else: raise Exception(f"add(g, item): unknown item type [{type(item)}]")
  return item

def set_color(item: Node|Graph, background, boundary):
  if isinstance(item, Node):
    item.set("style", "filled") # TODO: safe add style
    item.set("fillcolor", background)
    item.set("color", boundary)
  elif isinstance(item, Graph):
    item.set("bgcolor", background)
    item.set("pencolor", boundary)
class Colors:
  # usage: set_color(item, *Colors.gray)
  #         background, boundary
  gray   = ("#F5F5F5", "#666666")
  blue   = ("#DAE8FC", "#6C8EBF")
  green  = ("#D5E8D4", "#82B366")
  orange = ("#FFE6CC", "#D79B00")
  yellow = ("#FFF2CC", "#D6B656")
  red    = ("#F8CECC", "#B85450")
  purple = ("#E1D5E7", "#9673A6")
