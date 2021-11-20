import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

arr = []


def dfs(s):
    # for문에서 모든 경우의 수를 볼 필요가 없고(board가 아니니까), graph[s] 안에 있는 것만 보면 된다.
    for i in graph[s]:
        if visited[i] == 0:
            # dfs를 수행하기 전에 visited를 체크하면 parents를 따로 체크할 필요가 없다.
            visited[i] = s
            dfs(i)


dfs(1)

for x in range(2, n+1):
    print(visited[x])
