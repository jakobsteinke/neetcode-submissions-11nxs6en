class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evalExpression(operand1, operand2, operator):
            op1 = int(operand1)
            op2 = int(operand2)
            match operator:
                case '+':
                    return op1 + op2
                case '-':
                    return op1 - op2
                case '*':
                    return op1 * op2
                case '/':
                    return int(op1 / op2)
                case _:
                    return 0
        
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/':
                operator = stack.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(evalExpression(operand1, operand2, operator))
        return stack[0]