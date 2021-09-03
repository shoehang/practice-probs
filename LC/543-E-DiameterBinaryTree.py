# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.currLongestPath = 0
        
        def dfs(node):
            if node is None:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                self.currLongestPath = max(self.currLongestPath, left + right + 1)
            return 1 + max(left, right)
        
        dfs(root)
        return self.currLongestPath - 1