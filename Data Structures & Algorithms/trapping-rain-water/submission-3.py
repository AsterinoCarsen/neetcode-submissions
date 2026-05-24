class Solution:
    def trap(self, height: List[int]) -> int:
        water = []
        n = len(height)

        for i in range(0, n):
            leftMax, rightMax = 0, 0

            for left in range(i - 1, -1, -1):
                if height[left] > leftMax:
                    leftMax = height[left]

            for right in range(i + 1, n, 1):
                if height[right] > rightMax:
                    rightMax = height[right]

            waterI = max((min(leftMax, rightMax) - height[i]), 0)
            water.append(waterI)

        return sum(water)
