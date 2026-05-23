class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        numbers = set(nums)
        out = []

        for i in range(n):
            for j in range(n):
                k = -nums[i] - nums[j]
                if k in numbers:
                    kIndex = nums.index(k)
                    toAdd = sorted([nums[i], nums[j], k])
                    if i != j and j != kIndex and i != kIndex and toAdd not in out:
                        out.append(toAdd)

        return out