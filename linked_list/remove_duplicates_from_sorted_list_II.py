# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Remove Duplicates from Sorted List II
    https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        duplecate_index = {}
        
        current_node = head
        i = 0
        while current_node!=None:
            next_node = current_node.next
            if next_node!=None and current_node.val == next_node.val:
                current_node.next = next_node.next
                duplecate_index[i] = 0
            else:
                current_node = current_node.next
                i+=1
                
        current_node = head
        j = 0
        while current_node!=None:
            if j+1 in duplecate_index:
                next_node = current_node.next
                current_node.next = next_node.next         
            else:
                current_node = current_node.next
                
            j+=1
            
        k=0
        if k in duplecate_index:
            return head.next
        
        return head
        