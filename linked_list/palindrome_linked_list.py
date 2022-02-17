class Solution:
    """
    Palindrome Linked List
    https://leetcode.com/problems/palindrome-linked-list/
    
    """
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        num = ""
        current_node = head
        
        while current_node!=None:
            num+=str(current_node.val)
            current_node = current_node.next
            
        i,k=0,len(num)
        while i < k:
            if num[i]!=num[k-1]:
                return False
            i+=1
            k-=1

        return True