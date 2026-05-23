class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for left in range(n):
            for right in range(left + 1, n):
                res = numbers[left] + numbers[right]
                if res == target:
                    return [left + 1, right + 1]

        return [-1, -1]