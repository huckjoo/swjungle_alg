import sys

data = sys.stdin.readline().split('-')
first = 0

first_data = data[0].split('+')
for x in first_data:
    first += int(x)
cnt = 0
for i in range(1, len(data)):
    nums = data[i].split('+')
    for x in nums:
        cnt += int(x)
print(first-cnt)
