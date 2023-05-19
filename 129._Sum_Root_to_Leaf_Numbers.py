# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def backtrack(root, collect):
            if not root:
                return 0
               
            #pre order
            collect += str(root.val)
            
            if not root.left and not root.right:
                self.res += int(collect)
                
            backtrack(root.left, collect)
            backtrack(root.right, collect)
            #print(collect)
        backtrack(root, "")
        print(self.res)
            
        return self.res
            
            
            
            
            
            
            
            
