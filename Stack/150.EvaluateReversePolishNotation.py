class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        match token := tokens.pop():
            case '+':
                left = self.evalRPN(tokens)
                right = self.evalRPN(tokens)
                return right + left
            case '-':
                left = self.evalRPN(tokens)
                right = self.evalRPN(tokens)
                return right - left
            case '*': 
                left = self.evalRPN(tokens)
                right = self.evalRPN(tokens)
                return right * left
            case '/':
                left = self.evalRPN(tokens)
                right = self.evalRPN(tokens)
                return math.trunc(right / left)
            case _:
                return int(token) 
        
