# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None 
        self.isfound = False
        self.k = k
        def traverse(root):
            if self.isfound:
                return 
            if not root:
                return 
            
            left = traverse(root.left)
            self.k -= 1 
            if self.k == 0 :
                self.ans = root.val 
                self.isfound = True
                return 
            
            right = traverse(root.right)
            
            # return min(left, right)
        traverse(root)
        return self.ans
