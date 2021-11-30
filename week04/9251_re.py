import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
a_length = len(A)
b_length = len(B)

dp = [[0]*(a_length+1) for _ in range(b_length+1)]

for y in range(1, b_length+1):
    for x in range(1, a_length+1):
        if B[y-1] == A[x-1]:
            dp[y][x] = dp[y-1][x-1]+1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])

print(dp[b_length][a_length])
