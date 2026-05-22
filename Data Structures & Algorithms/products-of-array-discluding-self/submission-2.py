class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            arr = [nums[j] for j in range(len(nums)) if i != j]
            res = arr[0]
            for j in range(1, len(arr)):
                res *= arr[j]
            out.append(res)

        return out