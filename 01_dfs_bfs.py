from collections import deque

# Sample graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
    print()

# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run both traversals
start_node = 'A'
bfs(graph, start_node)
print("DFS Traversal:", end=" ")
dfs(graph, start_node)
