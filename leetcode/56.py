from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:  # List가 1개일 때
            return intervals
        ans = []
        intervals.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        lp = 0
        rp = 1
        length = len(intervals)

        new_start = intervals[lp][0]
        new_end = intervals[lp][1]

        while rp <= length-1:
            l_start = intervals[lp][0]
            l_end = intervals[lp][1]
            r_start = intervals[rp][0]
            r_end = intervals[rp][1]

            while new_start <= r_end:  # 겹치는 경우
                r_start = intervals[rp][0]
                r_end = intervals[rp][1]

                if r_start < new_start:
                    new_start = r_start
                rp += 1

                if rp >= length:
                    ans.append([new_start, new_end])
                    return ans

            ans.append([new_start, new_end])
            lp = rp
            rp = lp+1
            new_start = intervals[lp][0]
            new_end = intervals[lp][1]
            if rp >= length:
                ans.append([new_start, new_end])
        return ans
        # return sorted(ans)
