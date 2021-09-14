import sys

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        currMin, stack = sys.maxsize, [[root, 1]]
        
        while stack:
            node, depth = stack.pop()
            
            if node and not node.left and not node.right:
                currMin = min(depth, currMin)
                
            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return currMin