from collections import defaultdict
import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def __init__(self) -> None:
        tickets = [["JFK", "SFO"], ["JFK", "ATL"],
                   ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        print(self.findItinerary(tickets))

    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            print(route)
        visit('JFK')
        return route[::-1]


Solution()
