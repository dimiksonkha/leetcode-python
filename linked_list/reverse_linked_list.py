class Solution:
    """
    Reverse Linked List
    https://leetcode.com/problems/reverse-linked-list/

    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        current_head = head.next
        new_head = ListNode(head.val)
        
        while current_head!=None:
            temp = current_head.val
            new_head = ListNode(temp, new_head)
            current_head = current_head.next
        
        return new_head