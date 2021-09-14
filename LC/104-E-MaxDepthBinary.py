
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        currMax, stack = 0, [[root, 1]]
        
        while stack:
            node, depth = stack.pop()
            
            if node and not node.left and not node.right:
                currMax = max(depth, currMax)
                
            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return currMax