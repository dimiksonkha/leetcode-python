# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Delete the Middle Node of a Linked List
    https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
    
    """
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        current_node = head
        n=0
        
        while current_node != None:
            n+=1
            current_node = current_node.next
        
        current_node = head
        n = n//2
        for i in range(n-1):
            current_node = current_node.next
        next_node = current_node.next
        current_node.next = next_node.next
        
        return head
        