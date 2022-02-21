# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Convert Binary Number in a Linked List to Integer
    https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
    
    """
    def getDecimalValue(self, head: ListNode) -> int:
        if head.next == None:
            return head.val
        
        decimal_value = 0
        current_node = head
        n=0
        
        while current_node != None:
            n+=1
            current_node = current_node.next
        
        current_node = head
        for i in range(n-1,-1,-1):
            temp = current_node.val * (2**i)
            decimal_value+=temp
            current_node = current_node.next
            
        return decimal_value