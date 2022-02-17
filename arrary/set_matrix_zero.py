class Solution:
    """
    Set Matrix Zeroes
    https://leetcode.com/problems/set-matrix-zeroes/
    
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for p in range(n):
                        if matrix[i][p] != 0 and p!=j:
                            matrix[i][p] = None
                        
                    for q in range(m):
                        if matrix[q][j] != 0 and q!=i:
                            matrix[q][j] = None
                        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        