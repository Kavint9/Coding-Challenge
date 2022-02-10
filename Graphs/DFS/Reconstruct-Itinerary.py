# Leetcode problem: https://leetcode.com/problems/reconstruct-itinerary/
# Time Complexity: O(E^max) - E is number of flights, max is max number of flights leaving from any airport
# Space Complexity: O(E + V) - graph + visited
# Implicit Recusion, new_nodes dict useful to stop loops

from collections import defaultdict

class Solution:
    def backtracking(self, airport, route):
        # base condition
        if len(route) == self.length + 1:
            self.itinerary = route
            return True

        for i, ap in enumerate(self.adj_list[airport]):
            if not self.visited[airport][i]:
                self.visited[airport][i] = True
                if self.backtracking(ap, route + [ap]):
                    return True
                self.visited[airport][i] = False
        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.itinerary = []
        self.length = len(tickets)
        # create adj list - directed graph
        self.adj_list = defaultdict(list)

        self.visited = dict()
        for s, d in tickets:
            self.adj_list[s].append(d)

        for s, flights in self.adj_list.items():
            flights.sort()
            self.visited[s] = [False for _ in range(len(flights))]

        self.backtracking("JFK", ["JFK"])
        return self.itinerary
