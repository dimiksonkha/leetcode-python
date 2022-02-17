class Solution:
    """
    Rotate List
    https://leetcode.com/problems/rotate-list/
    
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        current_node = head
        
        while current_node != None:
            values.append(current_node.val)
            current_node = current_node.next
   
        n = len(values)
        if k > n and n!=0:
            k = n + (k%n)
        
        first_index = 0
        mid_index = n-k
        last_index = n
        
        part1 = values[first_index:mid_index]
        part2 = values[mid_index:last_index]
        values[:] = part2 + part1
        
        current_node = head
        for i in range(n):
            current_node.val = values[i]
            current_node = current_node.next
        
        return head