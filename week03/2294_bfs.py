# check를 만드는게 메모리를 훨씬 덜 사용한다.
# 왜냐하면 현재의 값을 저장하지 않으면, 1+1+1, 1+2, 3 등등 모든걸 queue에 넣어서 숫자가 커질수록 queue의 메모리가 기하급수적으로 커지기 때문이다.
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coins = []
ch = [False]*10001
for _ in range(n):
    now = int(sys.stdin.readline())
    if now <= k:
        if now not in coins:
            coins.append(now)

queue = deque()
queue.append((0, 0))  # coin값, cnt
while queue:
    now, cnt = queue.popleft()
    ch[now] = True
    for i in range(len(coins)):
        nxt = now + coins[i]
        if nxt <= k and ch[nxt] == False:
            ncnt = cnt + 1
            if nxt == k:
                print(ncnt)
                exit(0)
            ch[nxt] = True
            queue.append((nxt, ncnt))
print(-1)
