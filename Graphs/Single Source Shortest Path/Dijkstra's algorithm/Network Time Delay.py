# Leetcode problem: https://leetcode.com/problems/network-delay-time/
# Time Complexity: O(NM) M is max edges for any node
# Space Complexity: O(NE) the queue can have at most O(NE)
# Implement kruskal's algorithm
# for a weighted bidirectional graph sort in ascending order of weight and connect if no loops are formed

from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize
        adj = defaultdict(list)
        path = [list() for _ in range(n)]
        # adj list for edges and weights
        for s, d, w in times:
            edge = [d, w]
            adj[s].append(edge)

            # for dijkstra - vertices : [prev, weight]
        for i in range(1, n + 1):
            path[i - 1] = [0, sys.maxsize]

        path[k - 1] = [k, 0]
        queue = list()
        queue.append(k)
        while queue:
            # pop node and get current weight of node
            node = queue.pop(0)
            start, sw = path[node - 1]

            # check if the path matches
            for end, w in adj[node]:
                # Edge relaxation for neighbors
                prev, pw = path[end - 1]
                if sw + w < pw:
                    path[end - 1] = [start, sw + w]
                    # Add to queue the neighbor only if the value is changed
                    queue.append(end)

        # Dijkstra complete
        # check for max value
        val = -1
        for node, w in path:
            val = max(w, val)

        return val if val != sys.maxsize else -1








