# Leetcode problem: https://leetcode.com/problems/smallest-string-with-swaps/
# Time Complexity: O(LogN) for most operations, O(N) for constructor
# Space Complexity: O(N)
# Find connected components
# Rearrange the indexes of each connected components so that the letters are in lexicographical order
# Construct string from the rearranged strings


class UnionFind:
    def __init__(self, size):
        self.root = [ i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.connected_comp = {i :[i] for i in range(size)}

    def _connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def _find(self, v1):
        if v1 == self.root[v1]:
            return v1
        self.root[v1] = self._find(self.root[v1])
        return self.root[v1]

    def _union(self, v1, v2):
        r1 = self._find(v1)
        r2 = self._find(v2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
                arr = self.connected_comp.pop(r1, None)
                if arr:
                    self.connected_comp[r2].extend(arr)
            elif self.rank[r2] < self.rank[r1]:
                self.root[r2] = r1
                arr = self.connected_comp.pop(r2, None)
                if arr:
                    self.connected_comp[r1].extend(arr)
            else:
                self.root[r2] = r1
                arr = self.connected_comp.pop(r2, None)
                if arr:
                    self.connected_comp[r1].extend(arr)
                self.rank[r1] += 1

    def _get_connected_comp(self):
        return self.connected_comp


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(s) in [0, 1]:
            return s

        output = ['' for _ in range(len(s))]
        # Find the connected components
        inst = UnionFind(len(s))

        for i, j in pairs:
            inst._union(i, j)


        # iterate through connected components and sort the components
        for i, j in inst._get_connected_comp().items():
            j.sort()
            # sort components based on index
            arr = [[n, s[n]]  for n in j]
            # sort based on char
            sorted_arr = sorted(arr, key= lambda x: x[1])
            # final string will have lower index with lower char
            i = 0
            while i < len(j):
                output[arr[i][0]] = sorted_arr[i][1]
                i += 1

        # create output string
        string_out = ""
        for char in output:
            string_out += char

        return string_out

