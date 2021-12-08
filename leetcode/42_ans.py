# discuss 보고 푼 풀이
class Solution:
    def __init__(self) -> None:
        height = [4, 2, 0, 3, 2, 5]
        self.trap(height)

    def trap(self, height):
        # 컨셉은 현재 index에 저장된 물의 양은 index 기준 가장 큰 왼쪽 빌딩과 가장 큰 오른쪽 빌딩의 min값에 의해 좌우된다는 점이다.
        # 그리고 현재 있는 빌딩의 높이를 빼준다.
        water = [0] * len(height)
        left_max_list = [0] * len(height)
        right_max_list = [0] * len(height)
        left_max_val = 0
        right_max_val = 0
        # 각 idx마다 왼쪽 오른쪽 최대값이 다른데 그걸 설정해준다.
        for idx in range(len(height)):
            left_max_val = max(height[idx], left_max_val)
            left_max_list[idx] = left_max_val

        for idx in range(len(height)-1, -1, -1):
            right_max_val = max(height[idx], right_max_val)
            right_max_list[idx] = right_max_val
        # 각 idx마다 물의 높이를 구해서 더한다.
        for idx in range(len(height)):
            water[idx] = min(right_max_list[idx],
                             left_max_list[idx])-height[idx]
        return sum(water)


Solution()
