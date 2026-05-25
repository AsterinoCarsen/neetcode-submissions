class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            elif bracket in closing and stack:
                toCompare = stack.pop()
                if closing.index(bracket) != opening.index(toCompare):
                    return False
            else:
                return False
        return len(stack) == 0