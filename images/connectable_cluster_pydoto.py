from pydoto import CDot, addCCluster, addNode, addEdge

graph = CDot(label="Nodes and CClusters are all connectable")
graph.set_edge_defaults(minlen=3)

node00 = addNode(graph, "Node00")
node01 = addNode(graph, "Node01")
addEdge(graph, node00, node01)

node10 = addNode(graph, "Node10")
cluster11 = addCCluster(graph, "Cluster11")
node11 = addNode(cluster11, "Node11")
addEdge(graph, node10, cluster11)
addEdge(graph, node10, node11)

cluster20 = addCCluster(graph, "Cluster20")
node20 = addNode(cluster20, "Node20")
cluster21 = addCCluster(graph, "Cluster21")
node21 = addNode(cluster21, "Node21")
addEdge(graph, cluster20, cluster21)
addEdge(graph, node20, cluster21)
addEdge(graph, cluster20, node21)
addEdge(graph, node20, node21)

graph.write(__file__.replace(".py", ".dot"))
