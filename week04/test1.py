import sys

N = int(sys.stdin.readline())
meetings = []
for i in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# meetings.sort(key=lambda x: x[1])
# meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[0])
print(meetings)
