# Leetcode Problem: https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3845/
# Time Complexity: O(LogN)
# Space Complexity: O(N)


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def _connected(self, v1, v2):
        return self._find(v1) == self.find(v2)

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

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        inst = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    inst._union(i, j)
        return len([i for i in range(n) if i == inst.root[i]])

