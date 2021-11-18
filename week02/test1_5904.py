import sys
s0 = ['m', 'o', 'o']


def sol(n, k, l):                # n: Moo 수열의 n번째 글자(찾고자 하는 글자), # k: 차수, # l: 이전 차수의 길이
    # new_l: 새로운 차수의 길이 # 점화식 l(k) = l(k-1) + (k+3) + l(k-1)
    new_l = 2*l + k + 3
    if n <= 3:                   # n이 3 이하일 경우 바로 출력
        print(s0[n-1])
        exit(0)
    if new_l < n:                # new_l이 n보다 작을 경우
        sol(n, k+1, new_l)       # k 차수를 하나씩 늘려준다. new_l이 n을 담을 수 있을 때까지
    else:
        # n은 l보다 무조건 크기 때문에 생각하지 않는다. 원래 3파트로 나눠서 봐야하는데 2파트만 보면 된다.
        if n > l and n <= l+k+3:
            if n-l != 1:         # n-l = 1일때만 'm'이 있고 나머지는 'o'로 채워진다.
                print('o')
            else:
                print('m')
            exit(0)
        else:                    # 1+k+3 바깥에 있는 경우
            # [n - (1+k+3)]을 진행해서 다시 첫번째 part로 돌아온 다음 처음부터 재귀를 돌리기 시작한다.
            sol(n-(l+k+3), 1, 3)


n = int(sys.stdin.readline())
sol(n, 1, 3)
