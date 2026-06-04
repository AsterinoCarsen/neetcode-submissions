class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        n = len(s)
        maxLength = 0

        while right <= n:
            subStr = s[left : right]

            if self.containsDuplicate(subStr):
                left += 1
                right = left + 1
            elif len(subStr) > maxLength:
                maxLength = len(subStr)
                right += 1
            else:
                right += 1

        return maxLength


    def containsDuplicate(self, s: str) -> bool:
        return len(set(s)) != len(s)