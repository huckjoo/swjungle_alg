import sys

N = int(sys.stdin.readline())
stairs = []
dp = [0]*N

for i in range(N):
    stairs.append(int(sys.stdin.readline()))

for i in range(N):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = stairs[1] + stairs[0]
    elif i == 2:
        dp[2] = max((stairs[2]+stairs[1]), (stairs[2]+stairs[0]))
    else:
        dp[i] = max((stairs[i]+stairs[i-1]+dp[i-3]), (stairs[i]+dp[i-2]))

print(dp[-1])
