class Solution:
    """
    Swapping Nodes in a Linked List
    https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
    
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cn = head
        values = []
        
        while cn!=None:
            values.append(cn.val)
            n+=1
            cn = cn.next
        
        rev_k = n-k
        cn = head
        count = 1
        while cn!=None:
            if count == k:
                cn.val = values[rev_k]
            elif count == rev_k+1:
                cn.val = values[k-1]
            cn = cn.next
            count+=1
        
        return head