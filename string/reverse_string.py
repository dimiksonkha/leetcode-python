class Solution:
    """
    Reverse String
    https://leetcode.com/problems/reverse-string/
    
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,k=0,len(s)
        while i < k:
            temp = s[i]
            s[i]=s[k-1]
            s[k-1]=temp
            i+=1
            k-=1