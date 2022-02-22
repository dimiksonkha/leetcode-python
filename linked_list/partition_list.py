class Solution:
    """
    Partition List
    https://leetcode.com/problems/partition-list/
    
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        
        list_1 = []
        list_2 = []
        cn = head
        
        while cn!=None:
            if cn.val < x:
                list_1.append(cn.val)
            else:
                list_2.append(cn.val)
            cn = cn.next
            
        list_3 = list_1 + list_2
        n = len(list_3)
        cn = head
        
        for i in range(n):
            cn.val = list_3[i]
            cn = cn.next
            
        return head