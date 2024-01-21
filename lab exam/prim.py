import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.nodes = set()
        self.MST = []

    def addEdge(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append((d, w))
        self.graph[d].append((s, w))  # Assuming the graph is undirected
        self.nodes.add(s)
        self.nodes.add(d)

    def printSolution(self):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def primAlgo(self):
        start_node = next(iter(self.nodes))
        priority_queue = [(0, start_node)]
        visited = set()

        while priority_queue:
            weight, current_vertex = heapq.heappop(priority_queue)

            if current_vertex not in visited:
                visited.add(current_vertex)

                for neighbor, edge_weight in self.graph[current_vertex]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (edge_weight, neighbor))

                if weight > 0:
                    self.MST.append((current_vertex, neighbor, weight))

        self.printSolution()

# Example usage
g = Graph(5)
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.primAlgo()


        


        


















        





        

 


    




