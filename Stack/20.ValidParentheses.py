class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { '(' : ')', '{':'}', '[': ']'}
        lefts = ('(','{','[')
        for bracket in s:
            if bracket in lefts:
                stack.append(bracket)
            else:
                if not stack or not brackets[stack.pop()] == bracket:
                    return False
        return not stack
