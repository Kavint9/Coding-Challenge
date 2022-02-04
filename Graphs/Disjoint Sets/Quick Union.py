# Time complexity = O(N) for find and connected
# Space complexity = O(1) for union
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def find(self, vertex):
        current = vertex
        while current != self.root[current]:
            current = self.root[current]
        return current

    def union(self, v1, v2):
        p1 = self.find(v1) # This is used so that we can implement quick find along with quick union we connect to root
        p2 = self.find(v2)
        if p1 != p2:
            self.root[p2] = p1 # important roots are connected and not the children

    # This is done because if we dont then when we check for connected the roots might not match 


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