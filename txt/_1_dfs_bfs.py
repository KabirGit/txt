from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Adjacency list representation of the graph
        self.adjlist = defaultdict(list)

    def add_edge(self, u, v, direction):
        """
        Add an edge to the graph.
        direction = 0 -> undirected graph
        direction = 1 -> directed graph
        """
        self.adjlist[u].append(v)
        if direction == 0:
            self.adjlist[v].append(u)

    def print_adjlist(self):
        """Print the adjacency list of the graph."""
        for node, neighbors in self.adjlist.items():
            print(f"{node} -> {', '.join(map(str, neighbors))}")

    def bfs(self, src):
        """Perform BFS traversal starting from the source node."""
        q = deque([src])
        visited = defaultdict(bool)
        visited[src] = True

        print("BFS Traversal:")
        while q:
            frontnode = q.popleft()
            print(frontnode, end=" ")

            for neighbor in self.adjlist[frontnode]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, node, visited):
        """Utility function for DFS traversal."""
        print(node, end=" ")
        visited[node] = True

        for neighbor in self.adjlist[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, src):
        """Perform DFS traversal starting from the source node."""
        visited = defaultdict(bool)
        print("DFS Traversal:")
        self.dfs_util(src, visited)
        print()


# Main function
if __name__ == "__main__":
    g = Graph()

    # Input the number of edges
    n = int(input("Enter the number of edges: "))

    # Input the edges
    print("Enter the edges (u, v, direction):")
    for _ in range(n):
        u, v, direction = map(int, input().split())
        g.add_edge(u, v, direction)

    # Print the adjacency list
    print("Adjacency List:")
    g.print_adjlist()

    # Input the starting node for BFS and DFS
    startnode = int(input("Enter the starting node for BFS and DFS traversal: "))

    # Perform BFS and DFS
    g.bfs(startnode)
    g.dfs(startnode)