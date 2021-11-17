import sys
n = int(sys.stdin.readline())  # 전체 용액 수
sols = list(map(int, sys.stdin.readline().split()))
sols.sort()

pl = 0
pr = n-1
ans = []
cmin = 2000000001
while pl < pr:
    mixed = sols[pr]+sols[pl]
    if mixed == 0:
        ans = [sols[pl], sols[pr]]
        break
    if mixed > 0:
        if cmin > abs(mixed):
            cmin = abs(mixed)
            ans = [sols[pl], sols[pr]]
        pr -= 1
    elif mixed < 0:
        if cmin > abs(mixed):
            cmin = abs(mixed)
            ans = [sols[pl], sols[pr]]
        pl += 1

print(ans[0], ans[1])
