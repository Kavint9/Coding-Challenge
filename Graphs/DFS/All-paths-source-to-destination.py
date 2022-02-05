# Leetcode problem: https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
# Time Complexity: O(E+V)
# Space Complexity: O(V)
# Start DFS from source (Explicit Stack)
# if destination is reached return True else False
# Visited is not necessary since it is a Directed Acyclic Graph


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # edge cases:
        if not graph or len(graph) == 1:
            return []

        # Initialize variables
        d = len(graph) - 1
        output = []
        stack = []
        stack.append([0, []])

        while stack:
            node, path = stack.pop()
            # update the variables with the new node
            path.append(node)

            # Base condition
            if node == d:
                output.append(path)
                continue

            # Add neighbors to the stack
            for j in graph[node]:
                stack.append([j, path[:]])

        return output
