## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Linked List Cycle
    https://leetcode.com/problems/linked-list-cycle/
    
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        current_node = head
        node_list = {}
        has_cycle = False
        
        while has_cycle != True :
            if current_node.next == None:
                return 
            elif current_node.next in node_list:
                has_cycle = True
            else:
                node_list[current_node] = 0
                current_node = current_node.next
        
        return has_cycle