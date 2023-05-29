"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0 
        
        mx = 0 
        for child in root.children:
            mx = max(mx, self.maxDepth(child))
        return mx + 1
