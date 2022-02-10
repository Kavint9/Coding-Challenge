# Leetcode problem: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Time Complexity: O(ElogE)
# Space Complexity: O(E + V) All possible edges + Union Find
# Implement kruskal's algorithm
# for a weighted bidirectional graph sort in ascending order of weight and connect if no loops are formed

class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

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
            elif self.rank[root2] < self.rank[root1]:
                self.root[root2] = root1
            else:
                self.root[root2] = root1
                self.rank[root1] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge = [i, j]
                heapq.heappush(edges, (cost, edge))

        inst = UnionFind(n)
        output = 0
        count = n - 1
        while edges and count > 0:
            cost, edge = heapq.heappop(edges)
            v1 = edge[0]
            v2 = edge[1]
            if not inst._connected(v1, v2):
                inst._union(v1, v2)
                output += cost
                count -= 1

        return output




