import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

cnt = 0

for coin in coins:
    if coin <= K:
        cnt += K//coin
        K = K % coin

print(cnt)
