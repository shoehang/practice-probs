# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.dfs(root):
            return root
        return None
        
    def dfs(self, node):
        if not node:
            return True
        
        #travel down left     
        #travel down right
        left, right = self.dfs(node.left), self.dfs(node.right)
        
        #remove if 1 not found
        if left:
            node.left = None
        
        if right:
            node.right = None
        
        return left and right and node.val == 0