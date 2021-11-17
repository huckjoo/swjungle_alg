import sys
a, b, c = map(int, sys.stdin.readline().split())


def DAC(a, b, c):
    if b == 1:
        return a % c
    temp = DAC(a, b//2, c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


print(DAC(a, b, c))
