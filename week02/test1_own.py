import sys
s0 = ["m", "o", "o"]


def sol(n, k, l):
    new_l = 2*l + 3 + k
    if n <= 3:
        print(s0[n-1])
        exit(0)
    if new_l < n:
        sol(n, k+1, new_l)
    else:
        if n <= l + 3 + k:
            if n-l == 1:
                print("m")
            else:
                print('o')
            exit(0)
        else:
            sol(n-(l+3+k), 1, 3)


n = int(sys.stdin.readline())
sol(n, 1, 3)
