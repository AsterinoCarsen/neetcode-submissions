class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + j = target
        # j = target - i
        # i = target - j

        seen = dict() # index : nums[index]

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            
            seen[nums[i]] = i
        
        return [int('-inf'), int('-inf')]