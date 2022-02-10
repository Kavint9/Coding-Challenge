# Leetcode problem: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Time Complexity: O(E + V) - E traversed to create adj. list, V traversed in BFS
# Space Complexity: O(E + V) adjacency list will have Edges + vertices
# Implicit Recusion, new_nodes dict useful to stop loops

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        visited = [False for _ in range(n)]

        for s, d in edges:
            adj_list[s].append(d)
            adj_list[d].append(s)

        queue = []
        queue.append(source)
        while queue:
            curr = queue.pop(0)

            if curr == destination:
                return True

            visited[curr] = True
            for neighbor in adj_list[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)
        return False
