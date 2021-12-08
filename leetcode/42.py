class Solution:
    def __init__(self) -> None:
        height = [4, 2, 0, 3, 2, 5]
        self.trap(height)

    def trap(self, height):
        # The concept here is water that is going to get stored above any building would depenf upon largest height of building to it's left
        # and also the largest height of building to it's right. You take the minimum of it as only till that height the water would accumulate
        # Now just subtract of height of the building you are currently at so you get the height of water above it.
        # 컨셉은 현재 index에 저장된 물의 양은 index 기준 가장 큰 왼쪽 빌딩과 가장 큰 오른쪽 빌딩의 min값에 의해 좌우된다는 점이다.
        # 그리고 현재 있는 빌딩의 높이를 빼준다.

        # Array that stores largest element to itself in left
        LeftMaxIncludingCurrent = [0] * len(height)
        # Array that stores largest element to itself in right
        RightMaxIncludingCurrent = [0] * len(height)
        # This is just for simplicity, you actually don't need it, just take some counter over here
        Water = [0] * len(height)

        maxLeft = 0
        maxRight = 0

        # Fill up the LeftMaxIncludingCurrent Array
        for index in range(len(height)):
            maxLeft = max(maxLeft, height[index])
            LeftMaxIncludingCurrent[index] = maxLeft
        # Fill up the RightMaxIncludingCurrent Array
        for index in range(len(height)-1, -1, -1):
            maxRight = max(maxRight, height[index])
            RightMaxIncludingCurrent[index] = maxRight

        # Find the height of the water as discussed above in the concept
        for index in range(len(height)):
            Water[index] = min(LeftMaxIncludingCurrent[index],
                               RightMaxIncludingCurrent[index]) - height[index]
        # Take the sum of water that accumulated above every other building to get total water that got accumulated.
        print(sum(Water))
        return sum(Water)


Solution()
