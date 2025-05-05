# Number of vertices in the graph
N = 5

# A large value to represent infinity
INF = 99999999

# Adjacency matrix representation of the graph
G = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]
]

# Array to track selected nodes
selected_node = [False] * N
selected_node[0] = True  # Start from the first node

# Counter for the number of edges in the MST
no_edge = 0

print("Edge : Weight\n")

# Prim's Algorithm
while no_edge < N - 1:
    minimum = INF
    a = 0
    b = 0

    # Iterate through all nodes to find the minimum edge
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                # Check if the edge is valid and has the smallest weight
                if not selected_node[n] and G[m][n]:
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(f"{a} - {b} : {G[a][b]}")
    selected_node[b] = True
    no_edge += 1