import sys
from collections import deque
n = int(sys.stdin.readline())

for i in range(n):
    q = deque()
    ps = sys.stdin.readline()
    flag = 0
    for j in range(len(ps)):
        if len(q) == 0:
            if ps[j] == ')':
                print("NO")
                flag = 1
                break
        if ps[j] == '(':
            q.append(1)
        elif ps[j] == ')':
            q.pop()
    if len(q) == 0:
        if flag == 0:
            print("YES")
    else:
        if flag == 0:
            print("NO")
