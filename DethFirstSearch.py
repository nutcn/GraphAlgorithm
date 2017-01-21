# coding = utf-8

import sys
from Graph import Graph

graph = Graph.Graph(directed=False)
vertex_A = graph.insert_vertex('A')
vertex_B = graph.insert_vertex('B')
vertex_C = graph.insert_vertex('C')
vertex_D = graph.insert_vertex('D')
vertex_X = graph.insert_vertex('X')

graph.insert_edge(vertex_A, vertex_B)
graph.insert_edge(vertex_A, vertex_C)
graph.insert_edge(vertex_C, vertex_D)
graph.insert_edge(vertex_D, vertex_A)


# travelDict = {}
# Graph.DFS(graph, vertex_A, travelDict)
# path_ad = Graph.construct_path(vertex_A, vertex_D, travelDict)
# print [vertex.element() for vertex in path_ad]

forest = Graph.DFS_complete(graph)
print [vertex.element() for vertex in forest.keys()]
