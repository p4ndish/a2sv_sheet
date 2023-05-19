class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        def dfs(path):
            if path[-1] == n-1:
                res.append(path)
                return 
            
            
            for i in graph[path[-1]]:
                dfs(path + [i])
                
            #print(path)
        
        res = []
        n = len(graph)
​
        #for i in range(len(graph)):
        dfs([0])
        return res
            
