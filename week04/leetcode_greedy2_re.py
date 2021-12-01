import heapq


def reconstructQueue(people):
    heap = []
    res = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    while heap:
        now = heapq.heappop(heap)
        res.insert(now[1], [-now[0], now[1]])
    return res


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

print(reconstructQueue(people))
