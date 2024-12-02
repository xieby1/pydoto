# PydotO

PydotO (Pydot Object-oriented) is an enhanced wrapper for [Pydot](https://github.com/pydot/pydot/),
that provides a more intuitive object-oriented interface for creating Graphviz diagrams

## Features

### Node/Edge/... Creation with Return Values

Create nodes and edges with a clean, fluent syntax that returns the created elements for further manipulation:

```python
graph = CDot("A simple pydoto image")
miao = addNode(graph, "miao")
wang = addNode(graph, "wang")
addEdge(graph, miao, wang)
```

**Example**: [images/simple_pydoto.py](https://github.com/xieby1/pydoto/blob/main/images/simple_pydoto.py):

![](https://xieby1.github.io/pydoto/simple_pydoto.svg)

### Connectable Clusters

Create hierarchical graphs with clusters that can be connected directly to nodes or other clusters:

```python
addEdge(graph, node00, node01)
addEdge(graph, node10, cluster11) # Connect cluster to node
addEdge(graph, cluster20, cluster21) # Connect clusters directly
```

**Example**: [connectable_cluster_pydoto.py](https://github.com/xieby1/pydoto/blob/main/images/connectable_cluster_pydoto.py):

![](https://xieby1.github.io/pydoto/connectable_cluster_pydoto.svg)

### Auto Style Transfer

Styles (colors and line widths) automatically propagate from nodes and clusters to their connected edges:

```python
node_src = addNode(graph, "Source_Node", penwidth=2)
set_color(node_src, *Colors.red)
addEdge(graph, node_src, node_dst)
...
```

**Example**: [transitivity_pydoto.py](https://github.com/xieby1/pydoto/blob/main/images/transitivity_pydoto.py):

![](https://xieby1.github.io/pydoto/transitivity_pydoto.svg)

### Polymorphism

Simplified graph construction with a unified `add()` method that handles multiple element types:

```python
add(graph, node)
add(graph, edge)
add(graph, cluster)
...
```

## Installation

### Method 1: Direct File Import

Requirements: [Pydot](https://github.com/pydot/pydot/)

* Download `pydoto.py` from the [repository](https://github.com/xieby1/pydoto/blob/main/pydoto.py)
* Place it in your project directory
* Import using `from pydoto import xxx`

### Method 2: Nix Integration

```nix
pydoto = pkgs.python3Packages.callPackage (pkgs.fetchFromGitHub {
  owner = "xieby1";
  repo = "pydoto";
  rev = <Git Commit Rev>;
  hash = <Hash>;
}) {}
```

