class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        uniqueNums = set(nums)
        longest = 0

        for i in range(n):
            start = nums[i]
            curr = 1
            while (start + 1) in uniqueNums:
                start += 1
                curr += 1
            
            if curr > longest:
                longest = curr
        
        return longest

