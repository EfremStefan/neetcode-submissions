class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens) != 0:
            element = tokens.pop(0)
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            elif element == "/":
                b = stack.pop()
                a = stack.pop()
                quotient = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    quotient = -quotient

                stack.append(quotient)
            else:
                stack.append(int(element))
        return int(stack.pop())

        