from pydoto import CDot, addNode, addEdge

graph = CDot("A simple pydoto image")
miao = addNode(graph, "miao")
wang = addNode(graph, "wang")
addEdge(graph, miao, wang)

graph.write(__file__.replace(".py", ".dot"))
