import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = []


def sol(x, y, n):
    paper_color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper_color != paper[i][j]:
                sol(x, y, n//2)
                sol(x+n//2, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y+n//2, n//2)
                # 얘가 없으면 틀리는데 왜 있어야할까? -> sol에서 빠져나올때 아래 함수들이 모두 실행되기 때문인것 같다.
                return
    if paper_color == 1:
        res.append(1)
    else:
        res.append(0)


sol(0, 0, n)
print(res.count(0))
print(res.count(1))
