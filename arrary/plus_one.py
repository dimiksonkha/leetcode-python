class Solution:
    """
    Plus One
    https://leetcode.com/problems/plus-one/
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        if digits[n-1] < 9 :
            digits[n-1] = digits[n-1] +1
        else:
            i = n-1
            while digits[i] == 9:
                digits[i] = 0
                i-=1
            if i < 0:
                digits.insert(0,1)
                
            else:
                digits[i] = digits[i] + 1
                
        return digits             