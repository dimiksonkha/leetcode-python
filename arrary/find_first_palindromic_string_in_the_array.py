class Solution:
    """
    Find First Palindromic String in the Array
    https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
    """
    def is_palindrome(self, word):
        i,k=0,len(word)
        while i < k:
            if word[i]!=word[k-1]:
                return False
            i+=1
            k-=1

        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word) == True:
                return word
        
        return ""        