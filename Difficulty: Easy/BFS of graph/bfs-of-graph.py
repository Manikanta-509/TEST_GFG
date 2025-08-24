class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        V = len(adj)          # Number of vertices
        visited = [False] * V # To keep track of visited nodes
        result = []

        # BFS for each component (in case graph is disconnected)
        for start in range(V):
            if not visited[start]:
                queue = [start]  # Initialize queue with start node
                visited[start] = True

                while queue:
                    node = queue.pop(0)   # Remove first element
                    result.append(node)

                    # Add all unvisited neighbors
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
        return result

        # code here