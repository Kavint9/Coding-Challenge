# Leetcode problem: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Time Complexity: O(ElogE) - heap
# Space Complexity: O(E + V) Heap would store all edges + visited all vertices
# Implement kruskal's algorithm
# for a weighted bidirectional graph sort in ascending order of weight and connect if no loops are formed

from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0

            # Initlialize variables
        edges = []
        n = len(points)
        output = 0

        # visited array
        visited = [False for _ in range(n)]
        visited[0] = True

        count = n - 1

        for j in range(n):
            x1, y1 = points[0]
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            heapq.heappush(edges, (cost, [0, j]))

        while count > 0:
            # pop minimum till node with no visited
            cost, edge = heapq.heappop(edges)

            if not visited[edge[1]]:
                # include in visited
                visited[edge[1]] = True
                # include in cost
                output += cost
                count -= 1
                # add all edges of that node
                for j in range(n):
                    x1, y1 = points[edge[1]]
                    x2, y2 = points[j]
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(edges, (cost, [edge[1], j]))

        return output














