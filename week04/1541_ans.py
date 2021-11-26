# 조건 사용할 필요 없는 깔끔한 코드
import sys
a = sys.stdin.readline().split('-')
print(a)
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
