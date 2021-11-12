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
    a = 0
    b = 1
    cnt = 1
    flag = 0
    while True:
        if cnt >= c:  # 끝에 도착하기 전에 c를 넘으면(간격이 너무 좁으면)
            flag = -1
            break
        if b >= n:  # 끝에 도착했다면,
            flag = 1
            break
        if houses[b]-houses[a] >= pc:  # 집끼리 간격이 최소간격인 pc보다 크면
            cnt += 1  # 설치
            a = b
            b = a + 1
        else:                        # 집끼리 간격이 너무 좁으면
            b += 1                   # 그 집은 건너뜀
    if flag == 1:  # 설치간격 좁히자!
        pmax = pc - 1
    elif flag == -1:  # 설치간격 늘리자!
        res.append(pc)
        pmin = pc + 1
print(max(res))
