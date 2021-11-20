import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)


def dfs(s, prev):
    visited[s] = prev
    for i in range(1, n+1):
        if visited[i] == 0 and i in graph[s]:
            visited[i] = s
            dfs(i, s)


dfs(1, 0)


for x in range(2, n+1):
    print(visited[x])
