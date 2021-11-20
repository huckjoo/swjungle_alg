import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = [[0]*(n+1) for i in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1

queue = deque()
cnt = 0
for x in range(1, n+1):
    if ch[x] == 0:
        queue.append(x)
        ch[x] = 1
        while queue:
            now = queue.popleft()
            for i in range(1, n+1):
                if ch[i] == 0 and board[now][i] == 1:
                    queue.append(i)
                    ch[i] = 1
        cnt += 1
print(cnt)
