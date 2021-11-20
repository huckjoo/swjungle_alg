# dfs를 이런식으로도 쓰는구나! 모든 경우의 수를 탐색할 때
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_result = -1000000001
min_result = 1000000001


def dfs(res, cnt, p, m, mul, div):
    # 종료조건
    global max_result
    global min_result
    if n == cnt+1:
        max_result = max(max_result, res)
        min_result = min(min_result, res)
        return
    if p:
        dfs(res+nums[cnt+1], cnt+1, p-1, m, mul, div)
    if m:
        dfs(res-nums[cnt+1], cnt+1, p, m-1, mul, div)
    if mul:
        dfs(res*nums[cnt+1], cnt+1, p, m, mul-1, div)
    if div:
        if res < 0:
            dfs(-((-res)//nums[cnt+1]), cnt+1, p, m, mul, div-1)
        else:
            dfs(res//nums[cnt+1], cnt+1, p, m, mul, div-1)


dfs(nums[0], 0, op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)
