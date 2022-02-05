# Leetcode problem: https://leetcode.com/problems/clone-graph/
# Time Complexity: O(E+V)
# Space Complexity: O(V)
# Implicit Recusion, new_nodes dict useful to stop loops

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_nodes = dict()
        def DFS(current):
            # base condition
            # Implicitly handled
            # recursive step
            # create node copy
            new_node = Node(current.val, [])
            # add reference to dictionary
            new_nodes[current] = new_node
            for neighbor in current.neighbors:
                # check if neighbor exists in dictionary
                if neighbor in new_nodes:
                    new_node.neighbors.append(new_nodes[neighbor])
                else:
                    new_node.neighbors.append(DFS(neighbor))
                    # new_node.neighbors.append(new_nodes.get(neighbor, DFS(neighbor)))
            return new_node

        return DFS(node) if node else node

