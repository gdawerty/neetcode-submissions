class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Check if first row has any zero
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        # Check if first col has any zero
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
        
        # Use first row and first column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Zero out rows based on markers in first column
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        
        # Zero out columns based on markers in first row
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        
        # Finally handle first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Finally handle first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
