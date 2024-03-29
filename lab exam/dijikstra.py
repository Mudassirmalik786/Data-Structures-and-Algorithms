from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def dijkstraAlgo(graph, initial):
        visited = {initial: 0}
        path = defaultdict(list)
        nodes = set(graph.nodes)

        while nodes:
            minNode = None
            for node in nodes:
                if node in visited:
                    if minNode is None or visited[node] < visited[minNode]:
                        minNode = node
            if minNode is None:
                break

            nodes.remove(minNode)
            currentWeight = visited[minNode]

            for edge in graph.edges[minNode]:
                weight = currentWeight + graph.distances[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)

        return visited, path

g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")

g.addEdge("A", "B", 6)
g.addEdge("A", "C", 8)

result = g.dijkstraAlgo("A")
print(result)





 

                          
            

          

