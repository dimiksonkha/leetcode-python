class Solution:
    """
    Binary Tree Inorder Traversal
    https://leetcode.com/problems/binary-tree-inorder-traversal/
    
    """
    def in_order(self,node, values):

        if node == None:
            return values
        
        if node.left != None:
            self.in_order(node.left,values)

        values.append(node.val)    

        if node.right!= None:    
            self.in_order(node.right,values)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.in_order(root,values)
        return values