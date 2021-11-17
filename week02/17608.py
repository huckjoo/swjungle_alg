import sys
from collections import deque
n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    num = int(sys.stdin.readline())
    q.append(num)

now = q.pop()
cnt = 1
while q:
    temp = q.pop()
    if temp > now:
        now = temp
        cnt += 1
print(cnt)
