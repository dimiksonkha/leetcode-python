class Solution:
    """
    Reorder List
    https://leetcode.com/problems/reorder-list/
    
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current_node = head
        node_list = []
        
        while current_node!=None:
            temp = ListNode(current_node.val)
            node_list.append(temp)
            current_node = current_node.next
            
        n = len(node_list)
        last_index = n-1
        indices = []
        
        for i in range(n//2):
            temp = [i,last_index-i]
            indices+=temp
            
        if n%2!=0:
            indices.append(n//2)
            
        head.next = None
        current_node = head
        
        for index in indices:
            if index == 0:
                continue
            if current_node!=None:
                current_node.next = node_list[index]
            current_node = current_node.next