import sys
sys.setrecursionlimit(10**9)
Y, X = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]


def dfs(y, x):
    visited[y][x] = 1
    if x+1 <= X-1 and visited[y][x+1] == 0 and board[y][x+1] != 0:
        dfs(y, x+1)
    if y+1 <= Y-1 and visited[y+1][x] == 0 and board[y+1][x] != 0:
        dfs(y+1, x)
    if 0 <= x-1 and visited[y][x-1] == 0 and board[y][x-1] != 0:
        dfs(y, x-1)
    if 0 <= y-1 and visited[y-1][x] == 0 and board[y-1][x] != 0:
        dfs(y-1, x)
    return


year = 0
while True:
    visited = [[0]*X for _ in range(Y)]
    new_board = [[0]*X for _ in range(Y)]
    # 빙산 개수 확인
    div = 0
    flag = 0
    for y in range(Y):
        for x in range(X):
            if div >= 2:
                print(year)
                exit(0)
            if board[y][x] != 0:
                flag += 1
                if visited[y][x] == 0:
                    div += 1
                    dfs(y, x)

    if flag == 0:
        print(0)
        exit(0)
    year += 1

    # year가 지나면 빙산이 녹음
    for y in range(Y):
        for x in range(X):
            cnt = 0
            if board[y][x] != 0:
                if 0 <= y-1:
                    if board[y-1][x] == 0:
                        cnt += 1
                if y+1 <= Y-1:
                    if board[y+1][x] == 0:
                        cnt += 1
                if 0 <= x-1:
                    if board[y][x-1] == 0:
                        cnt += 1
                if x+1 <= X-1:
                    if board[y][x+1] == 0:
                        cnt += 1
            if board[y][x] < cnt:  # 음수일 경우 0으로 만들어줌
                new_board[y][x] = 0
            else:
                new_board[y][x] = board[y][x]-cnt

    board = new_board
