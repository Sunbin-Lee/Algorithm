class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        
        row_check = [False for _ in range(m)]
        col_check = [False for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_check[i] = True
                    col_check[j] = True
                    
        for i in range(m):
            for j in range(n):
                if row_check[i] or col_check[j]:
                    matrix[i][j] = 0
                    