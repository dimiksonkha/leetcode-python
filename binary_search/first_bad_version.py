class Solution:
    """
    First Bad Version
    https://leetcode.com/problems/first-bad-version/
    
    """
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n
        
        low = 1
        high = n
        mid = low + (high - low)//2
        
        while low <= high:
            if isBadVersion(mid) == True:
                high = mid-1
                mid = low + (high - low)//2
            else:
                low = mid+1
                mid = low + (high - low)//2
               
        return mid+1 