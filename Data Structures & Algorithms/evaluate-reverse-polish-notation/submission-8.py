class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operators = "+-*/"
        for t in tokens:
            if t in operators:
                if t == "+":
                    res = int(stack[-1])+int(stack[-2])
                    stack.pop()
                    stack.pop()
                if t == "-":
                    res = int(stack[-2])-int(stack[-1])
                    stack.pop()
                    stack.pop()            
                if t == "*":
                    res = int(stack[-1])*int(stack[-2])
                    stack.pop()
                    stack.pop()
                if t == "/":
                    res = int(int(stack[-2])/int(stack[-1]))
                    stack.pop()
                    stack.pop()     
                stack.append(res)            
            else:
                stack.append(t)
        return int(stack[-1])
