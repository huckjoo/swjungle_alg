# 스택 라이브러리 사용 > 왜 안되냐
from collections import deque

import sys

n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        q.append(int(data[1]))
    if data[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(-1))
    if data[0] == 'size':
        print(len(q))
    if data[0] == 'top':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    if data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
