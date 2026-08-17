class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose using bottom or upper triangle

        start = 0
        end = len(matrix) - 1

        while start < end: #swap rows, 1 -> last..
            temp = matrix[start]
            matrix[start] = matrix[end]
            matrix[end] = temp
            start +=1
            end -=1

        #transpose using bottom or upper triangle
        for row in range(len(matrix)):
            for col in range(row + 1): #bottom left triangle
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp


        