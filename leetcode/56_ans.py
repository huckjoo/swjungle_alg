class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            # merged intervals의 list가 비어있거나 현재 interval이 이전값과 overlap 되지 않는다면, just append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # overlap이 존재하면 현재, 이전 intervals를 merge 한다.
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
