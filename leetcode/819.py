from typing import List
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        banned = set(banned)  # 더 빠른 실행속도를 위해 set을 사용 (4ms 단축)
        int_dict = defaultdict(int)  # 없는값이 들어오면 0으로 초기화
        for i in range(len(symbols)):
            # 붙여서 들어오는 edge case 방어, split()은 모든 공백 제거
            paragraph = paragraph.replace(symbols[i], " ")
        paragraph = paragraph.lower().split()
        for word in paragraph:
            if word not in banned:
                int_dict[word] += 1
        sort_dict = sorted(int_dict.items(), key=lambda x: x[1])
        return sort_dict[-1][0]
