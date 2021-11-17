import sys

m, n, l = map(int, sys.stdin.readline().split())

gun_pos = list(map(int, sys.stdin.readline().split()))

gun_pos.sort()
animals = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b <= l:  # l보다 b(동물의 y축 좌표)가 작아야 쏠 수 있다.
        animals.append([a, b])
ans = 0
# 각 동물마다 사대에서 쏠 수 있는지만 체크
for x, y in animals:
    s = 0  # gun_pos list안에 있는 첫 번째 원소 접근
    e = len(gun_pos)-1  # gun_pos list안에 있는 마지막 원소 접근
    while s <= e:  # 이분탐색을 돌릴 때 s<=e로 =을 포함시켜줘야 한다. 그렇지 않으면 못보는 것들이 생긴다.
        mid = (s+e)//2
        if abs(gun_pos[mid]-x) + y <= l:  # 안에 들어온다.
            ans += 1
            break
        else:
            if gun_pos[mid] < x:  # 동물보다 현재 찾은 gun_pos의 x축위치가 작으면
                s = mid + 1
            else:
                e = mid - 1
print(ans)
