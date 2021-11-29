from sys import stdin
N, K = map(int, stdin.readline().split())
multitap = [0] * N
li = list(map(int, stdin.readline().split()))
res = swap = num = max_I = 0
for x in li:
    if x in multitap:  # 멀티탭에 이미 사용할 제품이 꽂혀있으면 pass
        pass
    elif 0 in multitap:  # 사용할 제품이 없는데 멀티탭에 빈칸이 있으면
        multitap[multitap.index(0)] = x  # 0 index에 사용할 제품을 꽂아
    else:                # 사용할 제품도 없고 자리도 없다면,
        for j in multitap:         # 멀티탭에 꽂혀있는 제품들 중에
            if j not in li[num:]:  # 이후로 사용하지 않는다면,
                swap = j           # swap 변수에 제품을 넣고 break시킨다.
                break
            elif li[num:].index(j) > max_I:  # 이후로 사용되는데, 사용되는 index가 max_I 보다 크다면
                max_I = li[num:].index(j)   # max_I를 걔로 바꿔주고 그 제품을 swap에 넣는다.
                swap = j
        multitap[multitap.index(swap)] = x  # swap의 인덱스에다가 쓰고 싶은 제품을 넣어준다.
        max_I = swap = 0                    # 초기화
        res += 1                            # 정답 += 1
    num += 1                                # num으로 이후에 들어오는 제품들 사용여부 체크
print(res)
