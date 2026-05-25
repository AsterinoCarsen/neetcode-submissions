class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket not in matches:
                stack.append(bracket)
            elif stack:
                toCompare = stack.pop()
                if matches[bracket] != toCompare:
                    return False
            else:
                return False
        return len(stack) == 0