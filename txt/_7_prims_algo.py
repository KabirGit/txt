import heapq

def prim(graph):
    n = len(graph)  # Number of nodes in the graph
    visited = [False] * n  # Track visited nodes
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent_node)
    total_cost = 0  # Total weight of the MST
    mst = []  # List to store edges in the MST

    while min_heap:
        # Pop the edge with the smallest weight
        weight, u, parent = heapq.heappop(min_heap)

        # If the node is already visited, skip it
        if visited[u]:
            continue

        # Mark the node as visited
        visited[u] = True
        total_cost += weight

        # If the edge is valid (not the starting node), add it to the MST
        if parent != -1:
            mst.append((parent, u, weight))

        # Add all unvisited neighbors of the current node to the heap
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost

# Example usage
graph_prim = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst_p, weight_p = prim(graph_prim)

# Print the edges in the MST
print("Edges in MST:")
for u, v, w in mst_p:
    print(f"{u} -- {v} == {w}")

# Print the total weight of the MST
print(f"Total weight: {weight_p}")