# kruskal 알고리즘 사용

# (cost, a, b) 순으로 만들어서 오름차순 정렬을 해 놓는다.
# 사이클이 발생하는 경우 그 cost는 포함하지 않는다.
# 사이클이 발새하지 않는 경우 cost를 포함하고, union 해준다.

import sys

V, E = map(int, sys.stdin.readline().split())
parent = [i for i in range(0, V+1)]
arr = []
res = 0
for i in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr.append((cost, a, b))


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])  # 루트를 찾아서 떠나는 거임
    return parent[x]


def union(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa != pb:
        if pa > pb:
            parent[pa] = pb
        else:
            parent[pb] = pa
    return


arr.sort()
for data in arr:
    cost, a, b = data[0], data[1], data[2]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        res += cost
    else:
        pass
print(res)
