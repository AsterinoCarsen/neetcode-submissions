class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixMax, suffixMax, water = [height[0]], [height[n - 1]], []

        for i in range(1, n):
            prefixMax.append(max(prefixMax[i - 1], height[i]))

        for i in range(n - 1, -1, -1):
            suffixMax.append(max(suffixMax[-1], height[i]))
        
        suffixMax = suffixMax[::-1]

        for i in range(n):
            water.append(min(prefixMax[i], suffixMax[i]) - height[i])

        return sum(water)