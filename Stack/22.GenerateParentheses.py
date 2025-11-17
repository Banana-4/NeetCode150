class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _gen(s, left, right):
            if left == n and right == n:
                result.append(s)
                return
            if left < n:
                _gen(s + '(', left + 1, right)
            if right < left:
                _gen(s + ')', left, right + 1)
        result = []
        _gen("", 0, 0)
        return result
