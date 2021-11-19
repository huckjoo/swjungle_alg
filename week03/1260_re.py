import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

board = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1

visited = [0]*(n+1)


def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and board[start][i] == 1:  # 연결 되어있는데 아직 안간 점
            dfs(i)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and board[a][i] == 1:
                queue.append(i)
                visited[i] = 1


dfs(v)
visited = [0]*(n+1)
print()
bfs(v)
