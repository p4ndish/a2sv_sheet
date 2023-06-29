# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path = 0 
        
        self.target = targetSum
        def recurse(root, p):
            if not root: 
                return 
            p += root.val
            if p == self.target:
                self.path += 1 
                # return 
            recurse(root.left, p)
            recurse(root.right, p)
        def traverse(root):
            if not root:
                return 
            
            recurse(root, 0)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.path
            
            
