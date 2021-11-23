import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
board = [[list(map(int, sys.stdin.readline().split()))
          for _ in range(n)] for _ in range(h)]
queue = deque()
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 1:
                queue.append((z, y, x))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        ny = y + dy[i]
        nx = x + dx[i]
        nz = z + dz[i]
        if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h:  # 갈 수 있으면
            if board[nz][ny][nx] == 0:  # 한 번도 가지 않은 길이면
                board[nz][ny][nx] = board[z][y][x] + 1
                queue.append((nz, ny, nx))
maximum = -2
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0:
                print(-1)
                exit(0)
            if board[k][i][j] > maximum:
                maximum = board[k][i][j]

print(maximum - 1)
