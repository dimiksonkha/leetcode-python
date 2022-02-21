# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Remove Nth Node From End of List
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        current_node = head
        m=0
        
        while current_node != None:
            m+=1
            current_node = current_node.next
        
        current_node = head
        m = m-n
        
        if m == 0:
            return head.next
        
        for i in range(m-1):
            current_node = current_node.next
            
        next_node = current_node.next
        current_node.next = next_node.next
        
        return head