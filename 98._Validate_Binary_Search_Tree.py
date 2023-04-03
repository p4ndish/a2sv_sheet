# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root, valL, valR):
            if not root:
                return True
            if not (root.val<valR  and root.val>valL):
                return False
            left =  solve(root.left, valL , root.val)
            right = solve(root.right, root.val , valR)
            return left and right
            # if not left or not right:
            #     return False
            # else:
            #     return True
        return solve(root, -inf, inf)
