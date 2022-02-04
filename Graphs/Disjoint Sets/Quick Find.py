# TIme Complexity - O(1) for find and connected O(N) for union
# Space Complexity - O(N) root array where N is the number of nodes or vertices
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def find(self, vertex):
        return self.root[vertex]

    def union(self, vertex1, vertex2):
        parent2 = self.find(vertex2)
        parent1 = self.find(vertex1)
        if parent2 != parent1:
            for i in range(len(self.root)):
                if self.root[i] == parent2:
                    self.root[i] = parent1

    def print(self):
        print(self.root)

# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true

