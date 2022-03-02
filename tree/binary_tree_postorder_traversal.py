class Solution:
    """
    Binary Tree Postorder Traversal
    https://leetcode.com/problems/binary-tree-postorder-traversal/
    
    """
    def post_order(self,node,values):
        
        if node == None:
            return values

        if node.left != None:
            self.post_order(node.left,values)

        if node.right!= None:    
            self.post_order(node.right,values) 

        values.append(node.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.post_order(root,values)
        return values