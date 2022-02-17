class Solution:
    """
    Pascal's Triangle II
    https://leetcode.com/problems/pascals-triangle-ii/
    """
    def factorial(n):
        fact = 1
        while n > 0:
            fact *= n
            n-=1
        return fact
    
    def getRow(self, rowIndex: int) -> List[int]:
            row = [ factorial(rowIndex)//(factorial(i)*factorial(rowIndex-i)) for i in range(rowIndex+1)]
            return row