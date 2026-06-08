class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        maxLength = 0

        while left < right and right <= len(s):
            subStr = s[left : right]
            occurs = defaultdict(int)
            for char in subStr:
                occurs[char] += 1
            
            maxChar = max(occurs, key=occurs.get)
            isValid = (sum(occurs.values()) - occurs[maxChar]) <= k

            if isValid:
                maxLength = max(len(subStr), maxLength)
                right += 1
            else:
                left += 1
                right = left + 1

        return maxLength