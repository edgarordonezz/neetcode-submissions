class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    curr = num1 + num2
                    stack.append(curr)
                elif token == '-':
                    curr = num2 - num1
                    stack.append(curr)
                elif token == '*':
                    curr = num1 * num2
                    stack.append(curr)
                elif token == '/':
                    curr = int(num2 / num1)
                    stack.append(curr)
            else:
                stack.append(token)
        return int(stack[0])

            