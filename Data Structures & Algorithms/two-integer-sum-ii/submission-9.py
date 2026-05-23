class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum == target:
                return [left + 1, right + 1]

            if currSum > target:
                right -= 1
            if currSum < target:
                left += 1

        return [-1, -1]