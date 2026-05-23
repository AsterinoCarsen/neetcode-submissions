class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        uniqueNums = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in uniqueNums:
                curr = 1
                while (num + 1) in uniqueNums:
                    num += 1
                    curr += 1
                
                if curr > longest:
                    longest = curr
        
        return longest

