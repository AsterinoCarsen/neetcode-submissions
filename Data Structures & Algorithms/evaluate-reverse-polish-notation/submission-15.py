class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                res = self.evaluate(num1, num2, token)
                stack.append(res)
        
        return stack.pop()

    def evaluate(self, num1: int, num2: int, operator: str) -> int:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)
        else:
            return 1