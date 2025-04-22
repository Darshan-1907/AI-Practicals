import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f_score, node)
    came_from = {}  # To reconstruct path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current]:
            temp_g = g_score[current] + cost
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None  # No path found

# Sample graph (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Heuristic values (example: straight-line distances to goal 'F')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

path = a_star(graph, 'A', 'F', heuristic)
print("Shortest path from A to F:", path)
