import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (cost, current_node)
    pq = [(0, start)]
    visited = set()  # Set to track visited nodes
    distances = {node: float("inf") for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance to the start node is 0

    while pq:
        # Pop the node with the smallest cost
        cost, curr_node = heapq.heappop(pq)

        # If the current node is the destination, return the cost
        if curr_node == end:
            return cost

        # If the node is already visited, skip it
        if curr_node in visited:
            continue

        # Mark the current node as visited
        visited.add(curr_node)

        # Explore neighbors
        for next_node, edge_cost in graph[curr_node]:
            if next_node not in visited:
                new_cost = cost + edge_cost
                # If a shorter path is found, update the distance and push to the queue
                if new_cost < distances[next_node]:
                    distances[next_node] = new_cost
                    heapq.heappush(pq, (new_cost, next_node))

    # If the destination is unreachable, return infinity
    return float("inf")


# Graph represented as an adjacency list
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Find the shortest distance between two nodes
shortest_distance = dijkstra(graph, 'B', 'D')
print("The shortest distance between B and D is", shortest_distance)







# Take input from the user
# graph = {}
# n = int(input("Enter the number of nodes in the graph: "))
# print("Enter the edges in the format 'node1 node2 weight':")
# for _ in range(int(input("Enter the number of edges: "))):
#     u, v, w = input().split()
#     w = int(w)
#     if u not in graph:
#         graph[u] = []
#     if v not in graph:
#         graph[v] = []
#     graph[u].append((v, w))
#     graph[v].append((u, w))  # Assuming the graph is undirected

# start = input("Enter the start node: ")
# end = input("Enter the end node: ")

# # Find the shortest distance between two nodes
# shortest_distance = dijkstra(graph, start, end)
# if shortest_distance == float("inf"):
#     print(f"There is no path between {start} and {end}.")
# else:
#     print(f"The shortest distance between {start} and {end} is {shortest_distance}.")