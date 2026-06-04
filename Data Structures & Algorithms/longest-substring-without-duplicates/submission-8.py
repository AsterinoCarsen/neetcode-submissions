class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        maxLength = 0

        seen = set()

        while right < n:
            newChar = s[right]

            if newChar in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(newChar)
                maxLength = max(maxLength, right - left + 1)
                right += 1

        return maxLength