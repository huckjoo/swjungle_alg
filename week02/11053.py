import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(n):
    start = i
    cnt = 1
    end = i+1
    temp = nums[start]
    while True:
        if end > n-1:
            break
        if nums[end] > temp:
            cnt += 1
            temp = nums[end]
        end += 1
    res.append(cnt)

print(res)
