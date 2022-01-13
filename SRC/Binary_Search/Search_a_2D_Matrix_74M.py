class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m * n == 0:
            return False
        if m * n == 1:
            if matrix[0][0] == target:
                return True
            return False
        
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] < target:
                start = mid
            elif matrix[row][col] == target:
                end = mid
            else:
                end = mid
            
        if matrix[start // n][start % n] == target:
            return True
        if matrix[end // n][end % n] == target:
            return True
        
        return False
        
        
