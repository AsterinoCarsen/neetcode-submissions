class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        right = 1

        for left in range(n - 1):
            right = left + 1
            currSum = numbers[left] + numbers[right]

            while currSum < target and right < n - 1:
                right += 1
                currSum = numbers[left] + numbers[right]

            if currSum == target:
                return [left + 1, right + 1]

        return [-1, -1]