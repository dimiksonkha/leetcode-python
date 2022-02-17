class Solution:
    """
    Pascal's Triangle
    https://leetcode.com/problems/pascals-triangle/
    
    """
    def factorial(n):
        fact = 1
        while n > 0:
            fact *= n
            n-=1
        return fact

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [ factorial(i)//(factorial(j)*factorial(i-j)) for j in range(i+1)]
            triangle.append(row)
        
        return triangle