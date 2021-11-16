from collections import deque
import sys
n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]

k = int(sys.stdin.readline())
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 2

l = int(sys.stdin.readline())
changes = deque()
for _ in range(l):
    t, c = sys.stdin.readline().split()
    changes.append([t, c])

snake = deque()
snake.append([0, 0])  # 뱀이 [꼬리,꼬리,꼬리,머리] 이런식으로 있다고 생각
board[0][0] = 1
directions = deque(['r', 'd', 'l', 'u'])

x = 0
y = 0
type = directions[0]
time = 0
while 0 <= x <= n-1 and 0 <= y <= n-1:
    if len(changes) > 0 and int(changes[0][0]) == time:
        temp = changes.popleft()
        direction = temp[1]
        if direction == "D":
            directions.append(directions.popleft())
            type = directions[0]
        else:
            directions.appendleft(directions.pop())
            type = directions[0]
    if type == 'r':
        x += 1
        time += 1
        if 0 <= x <= n-1 and board[y][x] != 1:
            if board[y][x] == 0:
                snake.append([x, y])  # 머리 넣기
                board[y][x] = 1  # 현재 뱀 머리위치 표시
                tmp = snake.popleft()  # 꼬리 자르기
                board[tmp[1]][tmp[0]] = 0  # board에 뱀 자리 지우기
            elif board[y][x] == 2:
                snake.append([x, y])  # 머리 넣기
                board[y][x] = 1  # 현재 뱀 머리위치 표시
        else:
            break
    elif type == 'l':
        x -= 1
        time += 1
        if 0 <= x <= n-1 and board[y][x] != 1:
            snake.append([x, y])  # 머리 넣기
            if board[y][x] == 0:
                board[y][x] = 1  # 현재 뱀 머리위치 표시
                tmp = snake.popleft()  # 꼬리 자르기
                board[tmp[1]][tmp[0]] = 0  # board에 뱀 자리 지우기
            elif board[y][x] == 2:
                board[y][x] = 1
        else:
            break
    elif type == 'u':
        y -= 1
        time += 1
        if 0 <= y <= n-1 and board[y][x] != 1:
            snake.append([x, y])  # 머리 넣기
            if board[y][x] == 0:
                board[y][x] = 1  # 현재 뱀 머리위치 표시
                tmp = snake.popleft()  # 꼬리 자르기
                board[tmp[1]][tmp[0]] = 0  # board에 뱀 자리 지우기
            elif board[y][x] == 2:
                board[y][x] = 1
        else:
            break
    elif type == 'd':
        y += 1
        time += 1
        if 0 <= y <= n-1 and board[y][x] != 1:
            snake.append([x, y])  # 머리 넣기
            if board[y][x] == 0:
                board[y][x] = 1  # 현재 뱀 머리위치 표시
                tmp = snake.popleft()  # 꼬리 자르기
                board[tmp[1]][tmp[0]] = 0  # board에 뱀 자리 지우기
            elif board[y][x] == 2:
                board[y][x] = 1
        else:
            break

print(time)
