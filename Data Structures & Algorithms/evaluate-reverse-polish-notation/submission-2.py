class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None
        stack = []
        for t in tokens:
            # if t is an operator pop numbers
            if t in ("+", "-", "/", "*"): 
                b = stack.pop()
                a = stack.pop()
                # since t was an operator lets do the arithmetic
                if t == "+": 
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
            # t was not an operator so append numbers to stack
            else:
                stack.append(int(t))
        # return the computed number
        return stack.pop()