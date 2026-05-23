class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxWater = 0

        for left in range(n):
            for right in range(n):
                if left == right:
                    break
                
                storedWater = min(heights[left], heights[right]) * abs(right - left)
                if storedWater > maxWater:
                    maxWater = storedWater
        return maxWater
