class Solution:
    """
     Valid Perfect Square
     https://leetcode.com/problems/valid-perfect-square/
    """
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        low = 1
        high = num/2
        
        while low<=high:
            mid = (low + high)//2
            sqaure = mid*mid
            
            if sqaure == num:
                return True
            elif sqaure < num:
                low = mid+1
                
            elif sqaure > num:
                high = mid-1
            else:
                return False