# Introduction
Breadth-First Search (BFS) is a method used to traverse or search through a graph or tree. It explores nodes in layers — visiting all immediate neighbors of a node before moving deeper. It's widely used in real-world applications like finding shortest paths, web crawling, and network analysis.


Depth-First Search (DFS) is another common graph traversal algorithm. Unlike BFS, which explores nodes level by level, DFS dives as deep as possible into a branch before backtracking. It uses a stack (either manually or via recursion) to keep track of nodes to visit.

# Usage
BFS is commonly used in:

- Finding the shortest path in an unweighted graph.
- Web crawlers (exploring linked web pages).
- Social networking sites (e.g., finding people within 'k' degrees of connection).
- Solving puzzles like the shortest moves in a game.
- Network broadcasting (spreading messages in peer-to-peer networks).

DFS is useful when:

- You want to explore a graph deeply before exploring siblings.
- You're solving maze or puzzle-like problems.
- You want to check for cycles in a graph.
- You want to classify edges or build a topological order.

# Implementation Explained
Here’s how BFS works and how we implement it in Python:

1. Start from a given node (the source).

2. Use a queue to keep track of nodes to visit next.

3. Use a set to remember which nodes you've already visited (to avoid processing them again).

4. Repeat the process:

      -Remove a node from the front of the queue.

      -Visit it (print or process it).

      -Add all its unvisited neighbors to the queue.

5.Continue until the queue is empty.




DFS works like this:

1. Start at a given node.

2. Visit the node and mark it as visited.

3. For each of its unvisited neighbors, recursively apply DFS.

4. This continues until all reachable nodes are visited.

DFS can be implemented using:

- Recursion (simple and natural in Python)

- Or a stack (manual implementation)

# Example Graph
![Screenshot 2025-05-25 224407](https://github.com/user-attachments/assets/9cb737df-c41f-4aad-987e-cf13eb989f47)

A connects to B and C.

B connects to D and E.

C connects to F.

E also connects to F.


For a graph like this :




BFS (Breadth-First Search) Output: for command ( bfs(graph, 'A'))
Will get the output like this

A->
B->
C->
D->
E->
F

Why this output?

Start from A.
- Visit its neighbors → B and C.
- Then visit neighbors of B → D and E.
- Then visit neighbor of C → F.
- Lastly, E points to F, but F is already visited, so it's skipped.

BFS visits nodes in layers (or levels):

1. Level 0: A
2. Level 1: B, C
3. Level 2: D, E, F


Whereas DFS Depth-First Search output for above graph will look like this for command (dfs(graph, 'A'))

A->
B->
D->
E->
F->
C

Why this output?

DFS explores as deep as possible:

Start at A.

 - Go to B.

 - From B, go to D (no further neighbors).

 - Backtrack to B, then go to E → F.

  -Backtrack all the way, then explore remaining unvisited node: C (F already visited).

Note: The output may vary slightly depending on the order of neighbors in the graph dictionary.

#  Time and Space Complexity

FOR BFS:

Time Complexity: O(V + E)
V = number of vertices (nodes), E = number of edges (connections)

Space Complexity: O(V)

FOR DFS :

Time Complexity: O(V + E)
V = number of vertices (nodes), E = number of edges

Space Complexity:

O(V) for visited set

O(V) for recursive call stack (in worst-case for deep graphs)

# Differences 
![Screenshot 2025-05-25 230842](https://github.com/user-attachments/assets/73915e4a-fa5f-4dc5-9a1b-b200327df82c)













