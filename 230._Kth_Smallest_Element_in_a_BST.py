# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        # heapq.heapify(heap)
        
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            heapq.heappush(heap, root.val)
            traverse(root.right)
        traverse(root)
        heapq.heapify(heap)
        # print(dir(heapq))
        # print()
        return heapq.nsmallest(k, heap)[k-1]
