#include <iostream>
#include <queue>
#include <list>
using namespace std;

const int totalVertices = 10;

class Graph {
public:
    Graph() : vertexCount(0) {}

    void addVertex(int data) {
        if (vertexCount < totalVertices) {
            vertices[vertexCount] = data;
            vertexCount++;
        } else {
            cout << "Exceeded maximum number of vertices." << endl;
        }
    }
    // For undirected graph
    void addEdge(int from, int to) {
        adjacencyList[from].push_back(to);
        adjacencyList[to].push_back(from); 
    }

    void DFS(int start) {
        cout << "DFS: ";
        bool visited[totalVertices] = {false};
        DFSUtil(start, visited);
        cout << endl;
    }

    void BFS(int start) {
        cout << "BFS: ";
        bool visited[totalVertices] = {false};
        queue<int> q;

        visited[start] = true;
        q.push(start);
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            cout << current << " ";

            for (int neighbor : adjacencyList[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        cout << endl;
    }

    void DFSUtil(int vertex, bool visited[]) {
        visited[vertex] = true;
        cout << vertex << " ";

        for (int neighbor : adjacencyList[vertex]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    }
    int vertices[totalVertices];
    list<int> adjacencyList[totalVertices];
    int vertexCount;
};

int main() {
    Graph graph;

    // Add vertices
    for (int i = 1; i <= 5; ++i) {
        graph.addVertex(i);
    }

    // Add edges
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(2, 4);
    graph.addEdge(3, 5);

    // calling DFS and BFS
    graph.DFS(1);
    graph.BFS(1);

    return 0;
}


