class Solution:
    """
    Binary Tree Preorder Traversal
    https://leetcode.com/problems/binary-tree-preorder-traversal/
    
    """
    def pre_order(self,node, values):
        if node == None:
            return values
        
        values.append(node.val)

        if node.left != None:
            self.pre_order(node.left,values)

        if node.right!= None:    
            self.pre_order(node.right,values)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.pre_order(root, values)
        return values
        