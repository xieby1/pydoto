from pydoto import CDot, addCCluster, addNode, addEdge, set_color, Colors

graph = CDot(label="The colors and penwidth are defaultly transferred from Nodes/CClusters to Edges")

node_src = addNode(graph, "Source_Node", penwidth=2)
set_color(node_src, *Colors.red)
node_dst0 = addNode(graph, "node_dst0", label="Tranferred from Node to Edge")
addEdge(graph, node_src, node_dst0)

ccluster_src = addCCluster(graph, "Colored Cluster", penwidth=3)
addNode(ccluster_src, "Nested_Node")
set_color(ccluster_src, *Colors.blue)
node_dst1 = addNode(graph, "node_dst1", label="Tranferred from CCluster to Edge")
addEdge(graph, ccluster_src, node_dst1)

graph.write(__file__.replace(".py", ".dot"))
