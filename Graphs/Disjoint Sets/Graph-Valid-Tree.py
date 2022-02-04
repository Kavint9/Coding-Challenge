# Leetcode problem: https://leetcode.com/problems/graph-valid-tree/
# Time Complexity: O(LogN) for most operations, O(N) for constructor
# Space Complexity: O(N)
# Two conditions for a valid tree tree: 1 connected component with all the nodes, no. of edges is N-1

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.islands = size

    def _connected(self, v1, v2):
        return self._find(v1) == self._find(v2)

    def _find(self, v1):
        if v1 == self.root[v1]:
            return v1
        self.root[v1] = self._find(self.root[v1])
        return self.root[v1]

    def _union(self, v1, v2):
        root1 = self._find(v1)
        root2 = self._find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
            self.islands -= 1

    def _get_islands(self):
        return self.islands


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False

        inst = UnionFind(n)

        for i, j in edges:
            inst._union(i, j)
        return True if inst._get_islands() == 1 else False

