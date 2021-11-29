import sys

N, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
multitap = [0]*N

max_idx = res = now = swap = 0

for x in data:
    if x in multitap:
        pass
    elif 0 in multitap:
        multitap[multitap.index(0)] = x
    else:  # 다 꽂혀있고 중복되지도 않는 경우
        for used in multitap:
            if used not in data[now:]:
                swap = used
                break
            else:
                if data[now:].index(used) > max_idx:
                    max_idx = data[now:].index(used)
                    swap = used
        multitap[multitap.index(swap)] = x
        res += 1
        swap = max_idx = 0
    now += 1

print(res)
