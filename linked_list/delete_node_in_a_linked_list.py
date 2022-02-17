class Solution:
    """
    Delete Node in a Linked List
    https://leetcode.com/problems/delete-node-in-a-linked-list/
    
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next