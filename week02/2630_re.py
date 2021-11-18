import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = []


def sol(x, y, n):
    first_color = board[x][y]
    for i in range(x, x+n):  # 재귀함수가 돌 때마다 n의 범위도 줄어야 한다!
        for j in range(y, y+n):  # 이거 때문에 오류가 났음
            if first_color != board[i][j]:
                sol(x, y, n//2)
                sol(x+n//2, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    ans.append(first_color)


sol(0, 0, n)
print(ans.count(0))
print(ans.count(1))
