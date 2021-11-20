import sys
from collections import deque

n = int(sys.stdin.readline())
l = int(sys.stdin.readline())

board = [[0]*(n+1) for i in range(n+1)]

for i in range(l):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1

cnt = 0
ch = [0]*(n+1)

queue = deque()
queue.append(1)
ch[1] = 1
while queue:
    now = queue.popleft()
    cnt += 1
    for i in range(1, n + 1):
        if ch[i] == 0 and board[now][i] == 1:
            queue.append(i)
            ch[i] = 1

print(cnt-1)
