# 일단 넘기고 내일 물어보자
import sys

n = int(sys.stdin.readline())
in_out = sys.stdin.readline().strip()

graph = [[] for i in range(n+1)]  # 0 ~ n까지
visited = [0]*(n+1)
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break


def dfs(now):
    cnt = 0
    visited[now] = 1
    for x in graph[now]:
        if visited[x] == 0:        # 방문하지 않은 곳이고
            if in_out[x-1] == '0':  # 다음 dfs가 실외면,
                cnt += dfs(x)
            else:
                cnt += 1
    return cnt


for i in range(1, n+1):
    dfs(i)
