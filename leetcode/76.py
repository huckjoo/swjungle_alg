from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        
        # 오른쪽 포인터 이동
        for right, char in enumerate(s,1):
            missing -= need[char] > 0 # 왼편의 True, False를 먼저 판단하고 True(필요문자)면 1, Flase면 0을 뺀다.
            need[char] -= 1 # 얘는 그냥 무조건 -1씩 한다.
            
            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0: # 왼쪽 포인터가 필요없는 문자를 가리키고 있으면 왼쪽 포인터 이동(슬라이딩윈도우 줄어듬)
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start: # 맨 처음이나, 현재 end-start보다 작은 window를 가진놈이 나타나면 바꿔주고 left 이동
                    start,end = left,right
                    need[s[left]] += 1
                    missing +=1
                    left += 1
        return s[start:end]