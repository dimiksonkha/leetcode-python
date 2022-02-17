class Solution:
    """
    Add Two Numbers
    https://leetcode.com/problems/add-two-numbers/
    
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_a = l1
        node_b = l2
        l3 = ListNode()
        node_c = l3
        
        temp_val = 0
        
        while node_a!=None or node_b!=None:
            if node_a!=None:
                a = node_a.val
            else:
                a = 0
            
            if node_b!=None:
                b = node_b.val
            else:
                b = 0
            c = a+b+temp_val
            
            if c >9:
                node_c.val = c%10
                temp_val = 1
            else:
                node_c.val = c
                temp_val = 0
            
            if node_a != None:
                node_a = node_a.next
            
            if node_b != None:
                node_b = node_b.next
            
            if node_a!=None or node_b!=None:
                node_c.next = ListNode()
                node_c = node_c.next
            else:
                if temp_val != 0:
                    node_c.next = ListNode(temp_val)
            
        return l3