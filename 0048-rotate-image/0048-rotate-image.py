import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        original = copy.deepcopy(matrix)
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = original[n-1-j][i]
        """
        Do not return anything, modify matrix in-place instead.
        """
        