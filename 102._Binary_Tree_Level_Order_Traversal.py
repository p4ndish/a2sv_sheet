# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        '''
        Question: given the root node find the node values that are in the same
        level 
        
        Solution: Using BFS : firstly we will record our current level and also
        we use a qeue to store the current childs of the node(popped) and if our 
        current node that has been popped is not the same level as the "global
        level " that means this node is the child and we update our result value
        with the nodes before our current node then appened this child current
        node in the queue increasing the level (node, level+1)
        
        '''
        def bfs(node):
            level = 0 
            currNodes = []
            res = []
            
            q = deque([(node, level)])
            while q :
                n, lvl = q.popleft()
                
                if not n :
                    continue 
                if level != lvl:
