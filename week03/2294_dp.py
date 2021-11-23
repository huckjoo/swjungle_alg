n, k = map(int, input().split())  # n: 동전의 종류, k: 가치의 합
c = []
for i in range(n):
    c.append(int(input()))
dp = [0] + [100001 for _ in range(k)]  # 0이 있어야 dp가 작동된다.
for i in c:  # c = 1,5,12
    for j in range(1, k+1):
        if j - i >= 0:
            # dp[j-i]+1 의 의미는 1부터 k까지 j를 돌리는데, 그때마다 i하나를 빼고 i 동전 한개(+1)를 쓰겠다는 의미이다.
            dp[j] = min(dp[j-i]+1, dp[j])
    print(dp)
if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)
