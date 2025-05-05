import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x  # X-coordinate of the node
        self.y = y  # Y-coordinate of the node
        self.cost = cost  # Cost of the node
        self.parent = parent  # Parent node for path reconstruction
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to the goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        # Comparison operator for priority queue (min-heap)
        return self.f < other.f

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_search(start, goal, grid):
    # Initialize start and goal nodes
    start_node = Node(start[0], start[1], grid[start[0]][start[1]])
    goal_node = Node(goal[0], goal[1], grid[goal[0]][goal[1]])

    # Priority queue (open list) and closed list
    open_list = []
    closed_list = set()

    # Add the start node to the open list
    heapq.heappush(open_list, start_node)

    while open_list:
        # Pop the node with the smallest f value
        current_node = heapq.heappop(open_list)

        # If the goal is reached, reconstruct the path
        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Return the path in the correct order

        # Mark the current node as visited
        closed_list.add((current_node.x, current_node.y))

        # Explore neighbors
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x = current_node.x + dx
            neighbor_y = current_node.y + dy

            # Check if the neighbor is within bounds
            if neighbor_x < 0 or neighbor_x >= len(grid) or neighbor_y < 0 or neighbor_y >= len(grid[0]):
                continue

            # Check if the neighbor is an obstacle or already visited
            if grid[neighbor_x][neighbor_y] == -1 or (neighbor_x, neighbor_y) in closed_list:
                continue

            # Create a neighbor node
            neighbor_node = Node(neighbor_x, neighbor_y, grid[neighbor_x][neighbor_y], current_node)
            neighbor_node.g = current_node.g + neighbor_node.cost
            neighbor_node.h = heuristic(neighbor_node, goal_node)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Add the neighbor to the open list
            heapq.heappush(open_list, neighbor_node)

    # If the goal is not reachable, return None
    return None

# Example usage
start = (0, 0)
goal = (3, 3)
grid = [
    [0, 1, 2, 3],
    [1, 2, -1, 4],
    [2, -1, 4, 5],
    [3, 4, 5, 6]
]

path = a_star_search(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found.")