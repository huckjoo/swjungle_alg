# 시간초과 코드 > 아무래도 pop(0)에서 시간복잡도가 크게 증가하는 것 같다.
import sys
n, k = map(int, sys.stdin.readline().split())
data = sys.stdin.readline().strip()
datas = []
for i in range(len(data)):
    datas.append(int(data[i]))
cnt = 0
stack = []
datas.reverse()

while len(stack) < n-k:
    maximum = -1
    if len(datas) == 1:
        stack.append(datas[-1])
        break
    if k-cnt == 0:
        for x in datas:
            stack.append(str(x))
        break
    for i in range(k-cnt+1):  # k-cnt: 지워야될 숫자 - 현재까지 지운 숫자
        if maximum < datas[i]:
            maximum = datas[i]

    p = 0
    while datas:
        if datas[p] != maximum:
            datas.pop(0)
            cnt += 1  # 지운 숫자
        else:
            temp = datas[p]
            datas.pop(0)
            stack.append(str(temp))
            break
print(''.join(stack))
