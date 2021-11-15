import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push':
        q.append(int(data[1]))
    elif data[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif data[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif data[0] == 'size':
        print(len(q))
    elif data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
