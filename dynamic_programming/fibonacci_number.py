class Solution:
    """
    Fibonacci Number
    https://leetcode.com/problems/fibonacci-number/
    """
    def fib(self, n: int) -> int:
        return int((1.618034 ** n - (1-1.618034) ** n)/ math.sqrt(5))