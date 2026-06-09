from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        needCount = len(need)

        left = 0
        result = [-1, -1]
        resultLen = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == needCount:
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                leftChar = s[left]
                window[leftChar] -= 1

                if (
                    leftChar in need
                    and window[leftChar] < need[leftChar]
                ):
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if resultLen != float("inf") else ""