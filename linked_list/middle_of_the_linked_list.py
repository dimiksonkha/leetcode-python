# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Middle of the Linked List
    https://leetcode.com/problems/middle-of-the-linked-list/

    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        current_node = head
        n=0
        
        while current_node != None:
            n+=1
            current_node = current_node.next
        
        current_node = head
        n = n//2
        for i in range(n):
            current_node = current_node.next
        
        return current_node