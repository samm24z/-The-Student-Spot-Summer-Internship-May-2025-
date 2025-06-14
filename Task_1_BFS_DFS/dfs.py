# DFS Program in Python using Recursion

# Graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set to keep track of visited nodes
# This 'visited' set is a global variable for this specific recursive implementation.
# For a more robust function, you might pass it as an argument or make it local to an outer wrapper function.
visited = set() 

def dfs(node):
    # If the node has not been visited
    if node not in visited:
        # Process the current node (e.g., print it)
        print(node, end=' ')
        # Mark the node as visited
        visited.add(node)
        # Recursively visit all unvisited neighbors
        for neighbor in graph[node]:
            dfs(neighbor)

# --- How to run the DFS ---
print("Depth-First Search starting from node A:")
dfs('A') # Start the DFS from node 'A'
print() # Add a newline at the end for clean output
