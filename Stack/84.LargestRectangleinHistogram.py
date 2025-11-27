class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            h = heights[i]
            start = i
            while stack and h <= stack[-1][0]:
                max_area = max(max_area, stack[-1][0] * (i - stack[-1][1]))
                start = stack.pop()[1] 
            stack.append((h, start))
        i = len(heights)
        while stack:
            max_area = max(max_area, stack[-1][0] * (i - stack[-1][1]))
            stack.pop()   
        return max_area    
