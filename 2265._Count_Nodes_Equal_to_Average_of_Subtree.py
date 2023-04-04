# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        
        
        def recurse(root):
            if not root:
                return 0,0
            #post order
            
            left_sums, left_cnts = recurse(root.left)
            right_sums, right_cnts = recurse(root.right)
            ro = root.val
            sums  = ro + left_sums + right_sums
            length = 1 + left_cnts + right_cnts
            avg = sums//length
            if avg == ro:
                self.res += 1
            return sums, length
            # print(arr, sums , res)
                
            # print(f"\t\t{root.val}")
            # print(f'left:{left}\tright:{right}')
            
        recurse(root)
        return self.res
