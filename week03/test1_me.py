import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())  # n은 크기, k는 바이러스종류

board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

S, X, Y = map(int, sys.stdin.readline().split())  # S초 뒤에 X,Y에 있는 바이러스
visited = [[False]*(n) for i in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
time = 0
virus = []
for x in range(n):
    for y in range(n):
        now = board[x][y]
        if now != 0:
            virus.append(now)
virus = set(virus)
virus = list(virus)
virus.sort()

for k in virus:
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False and board[x][y] == k:
                queue.append((k, x, y))
                visited[x][y] = True

while queue:
    if time == S:
        break
    if time >= 201:
        break
    k, x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if board[nx][ny] == 0:
                board[nx][ny] = k
                queue.append((k, nx, ny))
                visited[nx][ny] = True
                if nx == X-1 and ny == Y-1:
                    print(k)
                    exit(0)

print(board[X-1][Y-1])
