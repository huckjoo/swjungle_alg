import sys
from copy import deepcopy
from collections import deque

r, c = map(int, sys.stdin.readline().split())

data = [list(sys.stdin.readline().strip()) for i in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

hedgehog = deepcopy(data)
flood = deepcopy(data)

queue = deque()
# 홍수 움직임
for y in range(r):
    for x in range(c):
        if flood[y][x] == '*':
            flood[y][x] = -1
            queue.append((y, x, 0))
# 도치 움직임
for y in range(r):
    for x in range(c):
        if hedgehog[y][x] == 'S':
            hedgehog[y][x] = 0
            queue.append((y, x, 1))
while queue:
    y, x, flag = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if flag == 0:  # 물의 움직임
                if flood[ny][nx] == '.' or flood[ny][nx] == 'S':
                    flood[ny][nx] = -1
                    queue.append((ny, nx, 0))
            if flag == 1:  # 도치의 움직임
                if hedgehog[ny][nx] == '.' or hedgehog[ny][nx] == 'D':
                    if flood[ny][nx] == '.' or flood[ny][nx] == 'D':
                        if hedgehog[ny][nx] == 'D':  # 비버굴 도착
                            print(hedgehog[y][x]+1)
                            exit(0)
                        hedgehog[ny][nx] = hedgehog[y][x] + 1
                        queue.append((ny, nx, 1))
print("KAKTUS")
