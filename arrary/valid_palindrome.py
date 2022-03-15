import re
class Solution:
    """
    Valid Palindrome
    https://leetcode.com/problems/valid-palindrome/
    
    """
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        i,k=0,len(s)
        while i < k:
            if s[i]!=s[k-1]:
                return False
            i+=1
            k-=1

        return True