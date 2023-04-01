# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findpredi(root):
            if not root.right:
                return root.val
            return findpredi(root.right)
        
        
        def delete(root, prev, key):
            if not root:
                return
            #find
            if root.val > key:
                delete(root.left, root, key)
            elif root.val < key:
                delete(root.right, root, key)
            else:
                #check if leaf node
                if not root.left and not root.right:
                    #check if right or left
                    if prev.left and root.val == prev.left.val:
                        prev.left = None 
                    elif prev.right and root.val == prev.right.val:
                        prev.right = None
                #check if one node exist
                elif root.left and not root.right:
                    left = root.left  
                    root.val, root.left, root.right = left.val, left.left, left.right
                elif root.right and not root.left:
