from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_dict = defaultdict(int)
        for num in nums:
            int_dict[num] += 1
        new_dict = sorted(int_dict.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(new_dict[i][0])
        return ans
