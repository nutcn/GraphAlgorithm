# coding=utf-8

class Graph(object):

    class Vertex(object):
        __slots__ = '_element'

        def __init__(self, element):
            self._element = element
            
        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge(object):
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, origin, destination, element):
            self._origin = origin
            self._destination = destination
            self._element = element
            if not element:
                self._element = '%s->%s' % (origin.element(), destination.element())
            

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, vetex):
            return self._destination if vetex is self._origin else self._origin
            
        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        super(Graph, self).__init__()
        
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values)
        return result

    def get_edge(self, origin, destination):
        return self._outgoing[origin].get(destination)

    def degree(self, vetex, outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[vetex])

    def incident_edges(self, vetex, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[vetex].values():
            yield edge

    def insert_vertex(self, x=None):
        vetex = self.Vertex(x)
        self._outgoing[vetex] = {}
        if self.is_directed():
            self._incoming[vetex] = {}
        return vetex

    def insert_edge(self, origin, destination, element=None):
        edge = self.Edge(origin, destination, element)
        self._outgoing[origin][destination] = edge
        self._incoming[destination][origin] = edge

def DFS(graph, vertex, discoveredMap):
    ''' Depth First Search '''
    for edge in graph.incident_edges(vertex):
        next_vertex = edge.opposite(vertex)
        if next_vertex not in discoveredMap:
            discoveredMap[next_vertex] = edge
            DFS(graph, next_vertex, discoveredMap)

def construct_path(origin, dest, discoveredMap):
    path = []
    if dest in discoveredMap:
        path.append(dest)
        walk = dest
        while walk is not origin:
            edge = discoveredMap[walk]
            parent = edge.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def DFS_complete(graph):
    forest = {}
    for vertex in graph.vertices():
        if vertex not in forest:
            forest[vertex] = None # vertex as the root of a tree
            DFS(graph, vertex, forest)
    return forest

def BFS(graph, vertex, discoveredMap):
    level = [vertex]
    while len(level) > 0:
        next_level = []
        for edge in graph.incident_edges(vertex):
            next_vertex = edge.opposite(vertex)
            if next_vertex not in discoveredMap:
                discoveredMap[vertex] = edge
                next_level.append(next_vertex)
        level = next_level




