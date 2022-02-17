class Solution:
    """
    Reverse Integer
    https://leetcode.com/problems/reverse-integer/
    
    """
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x = x*-1
            y=-1
        else:
            y=1
            
        reverse_int = 0
        while x > 0:
            last_digit = x%10
            x//=10
            reverse_int = (reverse_int*10) + last_digit
    
        reverse_int*=y
        
        if reverse_int > (2**31)-1 or reverse_int < -2**31:
            return 0
        else:
            return reverse_int   
