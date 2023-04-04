# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        
        def recurse(preorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            i = 1 
            while i < len(preorder) and preorder[i] < root.val :
                i += 1 
                
            root.left = recurse(preorder[1:i])
            root.right = recurse(preorder[i:])
            
            return root
        return recurse(preorder)
        
        
#         root = TreeNode(preorder[0])
#         stack = [root]
        
#         for val in preorder[1:]:
#             if val < stack[-1].val:
#                 stack[-1].left = TreeNode(val)
#                 stack.append(stack[-1].left)
#             else:
#                 while stack and stack[-1].val < val:
