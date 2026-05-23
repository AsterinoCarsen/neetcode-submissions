class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        maxWater = 0

        while left < right:
            currWater = min(heights[left], heights[right]) * abs(right - left)

            if currWater > maxWater:
                maxWater = currWater

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater

