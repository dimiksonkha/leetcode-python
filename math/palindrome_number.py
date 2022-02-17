class Solution:
    """
    Palindrome Number
    https://leetcode.com/problems/palindrome-number/submissions/
    
    """
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return  True

        if x <0 or x%10 == 0:
            return False

        reverse_num = 0
        while x > reverse_num:
            last_digit = x%10
            x//=10
            reverse_num = (reverse_num*10) + last_digit

        if x == reverse_num or x == reverse_num//10:
            return True
        else:
            return False