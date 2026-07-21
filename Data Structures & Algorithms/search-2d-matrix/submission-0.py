class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS =len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = (ROWS*COLS) - 1

        while left <= right:
            mid = (left+right)//2

            row = mid//COLS
            col = mid%COLS

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                right = mid - 1
            
            else:
                left = mid + 1
            
        return False

            

