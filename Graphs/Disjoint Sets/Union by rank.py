# Time complexity = O(logN) for find and connected
# Space complexity = O(N) for union

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def _connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def _find(self, v):
        current = v
        while current != self.root[current]:
            current = self.root[current]
        return current

    def _union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        else:
            self.root[root1] = root2
            self.rank[root2] += 1

