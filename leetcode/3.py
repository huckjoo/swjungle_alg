class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_set = set()
        left_p = 0
        right_p = 0
        current_cnt = 1
        max_cnt = 1
        if len(s) > 0:
            current_set.add(s[left_p])
        else:
            return 0

        while left_p <= len(s)-2 and right_p <= len(s)-2 and left_p <= right_p:
            # right를 한칸 증가시킬 수 있을 경우
            if s[right_p + 1] not in current_set:
                right_p += 1
                current_set.add(s[right_p])
                current_cnt += 1
                if current_cnt > max_cnt:
                    max_cnt = current_cnt

            # right를 증가시킬 수 없어서 left를 증가시키는 경우
            elif(left_p + 1 <= right_p):
                current_set.remove(s[left_p])
                left_p += 1
                current_cnt -= 1

            # right도 left도 증가시킬 수 없는 경우
            else:
                left_p += 1
                right_p += 1
                current_cnt = 1

        return max_cnt
