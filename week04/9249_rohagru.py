import sys


def is_same_str(str1, str2, start1, start2, window_size):
    for w in range(window_size):
        if str1[start1 + w] != str2[start2 + w]:
            return False
    return True


def RabinKarp(word1, word2, ord_word1, ord_word2, window_size, constant):
    # q = 971
    # m = 29
    q = 1000000007
    m = 302
    hash_val = 0

    hash_list = [[] for _ in range(q)]
    for i in range(window_size):
        hash_val = (hash_val * m) % q
        hash_val = (hash_val + ord_word1[i]) % q
    hash_list[hash_val].append(0)

    for start_pos in range(1, len(word1)-window_size+1):
        hash_val *= m
        hash_val -= ord_word1[start_pos-1] * constant % q
        hash_val += ord_word1[start_pos+window_size-1]
        hash_val %= q
        hash_list[hash_val].append(start_pos)

    hash_val = 0
    for i in range(window_size):
        hash_val = (hash_val * m) % q
        hash_val = (hash_val + ord_word2[i]) % q
    for i in hash_list[hash_val]:
        if is_same_str(word1, word2, i, 0, window_size):
            return i

    for start_pos in range(1, len(word2)-window_size+1):
        hash_val *= m
        hash_val -= ord_word2[start_pos-1] * constant
        hash_val += ord_word2[start_pos+window_size-1]
        hash_val %= q

        for i in hash_list[hash_val]:
            if is_same_str(word1, word2, i, start_pos, window_size):
                return i


def find_longest_common_substring(word1, word2, ord_word1, ord_word2):
    # q = 971
    # m = 29
    q = 1000000007
    m = 302
    constants = [1] * 200001
    for i in range(1, 200000):
        constants[i] = constants[i-1] * m % q

    left = 1
    right = min(len(word1), len(word2))
    best = 0
    best_idx = 0
    while left <= right:
        mid = (left + right) // 2
        idx = RabinKarp(word1, word2, ord_word1,
                        ord_word2, mid, constants[mid])
        if idx is not None:
            left = mid + 1
            best = mid
            best_idx = idx
        else:
            right = mid - 1
    return best, word1[best_idx:best_idx+best]


if __name__ == '__main__':
    input = sys.stdin.readline
    word1 = input().rstrip()
    word2 = input().rstrip()
    ord_word1 = [ord(letter) - ord('a') for letter in word1]
    ord_word2 = [ord(letter) - ord('a') for letter in word2]

    print(*find_longest_common_substring(word1,
          word2, ord_word1, ord_word2), sep='\n')
