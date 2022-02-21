# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Linked List Cycle II
    https://leetcode.com/problems/linked-list-cycle-ii/
    
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        current_node = head
        node_list = {}
          
        while current_node!= None:
            if current_node.next in node_list:
                return current_node.next
            else:
                node_list[current_node] = 0
                current_node = current_node.next
        
        return None
        