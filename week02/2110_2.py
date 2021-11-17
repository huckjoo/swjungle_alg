# 1. while문을 for문으로 바꿔보자!
# 2. 배열에 넣어서 최대값을 찾지 말고 그냥 ans를 쓰자!
# 오히려 배열에 넣고 max 쓰는게 더 빠름 ;; 왜그런지 모르겠다.
import sys
n, c = map(int, sys.stdin.readline().split())
houses = []
for i in range(n):
    house = int(sys.stdin.readline())
    houses.append(house)
houses.sort()
pmin = 1
pmax = houses[-1]-houses[0]
ans = 0
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
        ans = pc
    else:
        pmax = pc - 1  # 다 돌고왔다면 설치간격 좁히자!
print(ans)
