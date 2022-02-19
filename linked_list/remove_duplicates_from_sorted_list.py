class Solution:
    """
    Remove Duplicates from Sorted List
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if head == None:
            return head
        
        while current_node!=None:
            next_node = current_node.next
            if next_node!=None and current_node.val == next_node.val:
                current_node.next = next_node.next
            else:
                current_node = current_node.next
            
        return head
