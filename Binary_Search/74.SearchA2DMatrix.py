class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0]) 
        height = len(matrix)
        end = width * height - 1
        start = 0
        while (start <= end):
            mid = (end + start) // 2
            row = mid // width
            column = mid % width
            if matrix[row][column] == target: return True
            elif matrix[row][column] > target: end = mid - 1
            else: start = mid + 1
        return False
