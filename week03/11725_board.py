# 메모리초과 코드
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())

board = [[0]*(n+1) for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1

visited = [0]*(n+1)

arr = []


def dfs(s, prev):
    arr.append((s, prev))
    visited[s] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and board[s][i] == 1:
            dfs(i, s)


dfs(1, 0)

arr.sort()
for i in range(1, n):
    print(arr[i][1])
