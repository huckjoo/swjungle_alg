import sys
from collections import deque
k = int(sys.stdin.readline())
q = deque()
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        q.pop()
    else:
        q.append(num)

if len(q) == 0:
    print(0)
else:
    print(sum(q))
