# 틀린이유: bfs를 board에 저장하고 1이 이어져 있으면 갔는데
# 지금 저장된 board의 1이라는 숫자는 a->b에서 갈 수 있다는 의미이므로
# 이렇게 사용하면 안될 것 같다.

# 입력
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# M개의 줄에 걸쳐서 A,B 공백을 기준으로 구분되어 주어짐, A!=B
import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, K, X = map(int, sys.stdin.readline().split())
board = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1


def bfs(y, x):
    flag = 0
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        print('y:', y, 'x:', x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        if 0 <= ny <= N and 0 <= nx <= N:
            if board[ny][nx] == 1:
                queue.append((ny, nx))
                board[ny][nx] = board[y][x] + 1
                if board[ny][nx] == K:
                    print(nx)

    return flag


bfs(X, X)
print('X:', X)
