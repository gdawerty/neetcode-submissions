class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = -1
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:  # target in this row range
                row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        if row == -1:
            return False
        start = 0
        end = len(matrix[row]) - 1
        while start <= end:
            mid = (start + end) // 2

            if matrix[row][mid] > target:
                end = mid - 1
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                return True
        return False
            
