# 150: Evaluate Reverse Polish Notation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def eval(operations):
            operation = operations.pop()
            second = operations.pop()
            first = operations.pop()

            if operation == "+":
                return int(first) + int(second)
            elif operation == "-":
                return int(first) - int(second)
            elif operation == "/":
                return int(first) / int(second)
            elif operation == "*":
                return int(first) * int(second)

        stack = []
        idx = 0

        while idx < len(tokens):
            ele = tokens[idx]
            idx += 1

            if ele is "+" or ele is "-" or ele is "/" or ele is "*":
                second = stack.pop()
                first = stack.pop()
                newCalc = eval([first, second, ele])
                stack.append(newCalc)
            else:
                stack.append(ele)

        result = math.floor(int(stack[-1]))
        return result

        
        
