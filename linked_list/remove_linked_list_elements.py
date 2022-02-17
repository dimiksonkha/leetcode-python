class Solution:
    """
    Remove Linked List Elements
    https://leetcode.com/problems/remove-linked-list-elements/
    
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        current_node = head
        
        while current_node.next!=None:
            if current_node.val == val:
                current_node.val = current_node.next.val
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next  

        if current_node.val == val and head.val== val:
            return None
        
        elif current_node.val == val:
            
            current_node = head
            while current_node.val!=val:
                temp_node = current_node.next
                if temp_node.val == val:
                    current_node.next = None
                current_node = temp_node    
        
        return head