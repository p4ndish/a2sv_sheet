# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        
        def recurse(root, path):
            if not root.left and not root.right:
                path += str(root.val)
                output.append(path)
                return 
            if root.left :
                recurse(root.left, path+str(root.val)+"->")
            if root.right:
                recurse(root.right, path+str(root.val)+"->")
                
        recurse(root, "")
        return output
            
