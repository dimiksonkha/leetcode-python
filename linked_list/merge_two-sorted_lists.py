class Solution:
    """
     Merge Two Sorted Lists
     https://leetcode.com/problems/merge-two-sorted-lists/
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        
        current_node_a = list1
        current_node_b = list2
        list3 = ListNode()
        current_node_c = list3
        
        while current_node_a!=None or current_node_b!=None:
            
            if current_node_a!=None and current_node_b!=None:
                if current_node_a.val == current_node_b.val:
                    
                    current_node_c.val = current_node_a.val
                    current_node_a = current_node_a.next
                    
                    current_node_c.next = ListNode()
                    current_node_c = current_node_c.next
                    
                    current_node_c.val = current_node_b.val
                    current_node_b = current_node_b.next

                    
                elif current_node_a.val < current_node_b.val:
                    current_node_c.val = current_node_a.val
                    current_node_a = current_node_a.next
                    
                else:
                    current_node_c.val = current_node_b.val
                    current_node_b = current_node_b.next
                    
                    
            elif current_node_a!=None and current_node_b==None:
                    current_node_c.val = current_node_a.val
                    current_node_a = current_node_a.next
                    
            elif current_node_a==None and current_node_b!=None:
                    current_node_c.val = current_node_b.val
                    current_node_b = current_node_b.next
                    
            if current_node_a!=None or current_node_b!=None:
                current_node_c.next = ListNode()
                current_node_c = current_node_c.next
                    
        return list3         