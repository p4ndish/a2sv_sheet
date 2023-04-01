# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def Lca(root, p, q):
            if not root:
                return root 
            
            if root.val < p.val and root.val < q.val:
                return Lca(root.right, p, q)
            elif root.val > p.val and root.val > q.val:
                return Lca(root.left, p, q)
            else:
                return root
        return Lca(root, p, q)
        # return 1
