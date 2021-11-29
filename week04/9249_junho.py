import sys

P = 29
mod = 10007

exp = [0 for _ in range(200000)]
for i in range(200000):
    if i == 0:
        exp[i] = 1
    else:
        exp[i] = exp[i - 1] * P % mod


def real_match(idx1, idx2, m):
    for i in range(m):
        if string1[idx1 + i] != string2[idx2 + i]:
            return False
    return True


string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
N1 = len(string1)
N2 = len(string2)


def solve(m):
    hash_list = [[] for _ in range(mod)]
    H = 0
    # string1
    for i in range(N1 - m + 1):
        if i == 0:
            for j in range(m):
                H *= P
                H += ord(string1[i + j]) - ord('a')
                H %= mod
            hash_list[H].append(i)
        else:
            H -= (ord(string1[i - 1]) - ord('a')) * exp[m - 1] % mod
            H = (H + mod) % mod
            H *= P
            H += ord(string1[i + m - 1]) - ord('a')
            H %= mod
            hash_list[H].append(i)
            '''
            if len(hash_list[H]):
                for j in range(len(hash_list[H])):
                    if real_match(hash_list[H][j], i, m):
                        return idx
                hash_list[H].append(i)
            else:
                hash_list[H].append(i)
            '''
    # string2
    H = 0
    for i in range(N2 - m + 1):
        if i == 0:
            for j in range(m):
                H *= P
                H += ord(string2[i + j]) - ord('a')
                H %= mod
        else:
            H -= (ord(string2[i - 1]) - ord('a')) * exp[m - 1] % mod
            H = (H + mod) % mod
            H *= P
            H += ord(string2[i + m - 1]) - ord('a')
            H %= mod
        if len(hash_list[H]):
            for j in range(len(hash_list[H])):
                if real_match(hash_list[H][j], i, m):
                    return hash_list[H][j]
    return -1


start = 0
end = min(N1, N2)

res = 0
idx = -1
while start < end:
    mid = (start + end + 1) // 2
    temp = solve(mid)
    if temp != -1:
        start = mid
        res = mid
        idx = temp
    else:
        end = mid - 1

print(res)
print(string1[idx:idx + res])
