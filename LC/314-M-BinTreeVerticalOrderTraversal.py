# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dq = collections.deque([])
        
        out = {}
        
        node = root
        
        if node is None:
            return []
        
        dq.append([node, 0])
    
        # O(V), V = # of nodes in tree
        while dq:
            node, col = dq.popleft()
            
            if col not in out:
                out[col] = [node.val]
            else:
                out[col].append(node.val)
                
            if node.left:
                dq.append([node.left, col - 1])
            if node.right:
                dq.append([node.right, col + 1])
        
        # O(2n), sorting  + formatting 
        return [out[i] for i in sorted(out.keys())]
    
    # T -> O(V + n)
    # S -> O(2V)