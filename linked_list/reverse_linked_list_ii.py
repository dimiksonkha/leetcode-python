class Solution:
    """
    Reverse Linked List II
    https://leetcode.com/problems/reverse-linked-list-ii/
    
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right ==1 :
            return head
        
        values = [None] * 500
        count = 0
        current_node = head
        rev_index = right-1
        
        while current_node!=None:
            
            if count+1 >= left and count+1 <=right:
                values[rev_index] = current_node.val
                rev_index-=1
                
            elif count+1 < left or count+1 > right:
                values[count] = current_node.val
                
            count+=1
            current_node = current_node.next
            
        current_node = head
        for i in range(count):
            current_node.val = values[i] 
            current_node = current_node.next    
            
        return head    
            