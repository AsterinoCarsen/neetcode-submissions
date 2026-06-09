class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        maxLength = 0
        occurs = defaultdict(int)
        occurs[s[left]] += 1
        occurs[s[right]] += 1

        while left < right and right <= len(s):
            maxChar = max(occurs, key=occurs.get)
            isValid = (sum(occurs.values()) - occurs[maxChar]) <= k

            if isValid:
                maxLength = max(len(s[left : right + 1]), maxLength)
                right += 1
            else:
                left += 1
                right = left + 1
                occurs.clear()
                occurs[s[left]] += 1
            
            if right < len(s):
                occurs[s[right]] += 1

        return maxLength