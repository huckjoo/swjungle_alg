# while문을 for문으로 바꿔보자!
import sys
n, c = map(int, sys.stdin.readline().split())
houses = []
for i in range(n):
    house = int(sys.stdin.readline())
    houses.append(house)
houses.sort()
pmin = 1
pmax = houses[-1]-houses[0]
res = []
while True:
    if pmin > pmax:  # while문 종료조건
        break
    pc = (pmin + pmax)//2
    current = houses[0]
    cnt = 1
    for i in range(1, n):
        if houses[i] - current >= pc:
            cnt += 1
            current = houses[i]
    if cnt >= c:  # 설치 간격 늘리자!
        pmin = pc + 1
        res.append(pc)
    else:
        pmax = pc - 1  # 다 돌고왔다면 설치간격 좁히자!
print(max(res))
