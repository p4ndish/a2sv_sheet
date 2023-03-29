# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def binsearch(root, val):
            if not root :
                return None
            if root.val == val:
                return root
            elif root.val > val:
                return binsearch(root.left, val)
            else:
                return binsearch(root.right, val)
                # return root
                # return result(root)
        # res = binsearch(root, val)
        return binsearch(root,val)
        # return ans if ans else None
