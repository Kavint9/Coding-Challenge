# Leetcode problem: https://leetcode.com/problems/smallest-string-with-swaps/
# Time Complexity: O(E+V)
# Space Complexity: O(N)
# Start DFS from source (Implicit/Recursive Stack)
# if destination is reached return True else False

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def DFS(node):
            # edge case
            if node == destination:
                return True

            # connected nodes
            for j in adj_list[node]:
                if not visited[j]:
                    visited[j] = True
                    # recursion => implicit stack is used
                    if DFS(j):
                        return True
                    # visited is not reverted here
                    # since if DFS from that node is false unnecessary to traverse that node again
            return False

        # create adj list
        adj_list = defaultdict(set)
        visited = [False for _ in range(n)]
        for s, d in edges:
            if (s == source and d == destination) or \
                    (d == source and s == destination):
                return True
            adj_list[s].add(d)
            adj_list[d].add(s)

        return DFS(source)



