
def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, color, v):
  
    if v == len(graph):
        return True


    for c in range(1, m + 1):
       
        if is_safe(graph, color, v, c):
            color[v] = c  

            
            if graph_coloring_util(graph, m, color, v + 1):
                return True

            
            color[v] = 0

    return False


def graph_coloring(graph, m):
    
    color = [0] * len(graph)


    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist.")
        return


    print("Coloring of vertices:")
    for i in range(len(graph)):
        print(f"Vertex {i + 1} ---> Color {color[i]}")


if __name__ == "__main__":
    # Example Graph (Adjacency Matrix)
    # 4 vertices, edges between 0-1, 0-2, 1-2, 1-3
    graph = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    m = 3  # Number of colors
    graph_coloring(graph, m)