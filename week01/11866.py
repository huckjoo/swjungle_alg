from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
yo = deque()
for i in range(1, n+1):
    yo.append(i)
ans = []
cnt = 1
while len(yo) > 0:
    for _ in range(k-1):
        yo.append(yo.popleft())
    ans.append(yo.popleft())


print('<', end='')
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end='')
    else:
        print(f'{ans[i]},', end=' ')
print('>', end='')
