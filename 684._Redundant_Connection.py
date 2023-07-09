class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        print(par)
        def find(node):
            # print(node)
            if par[node] == node:
                return node
            
            return find(par[node])
        
        
        def union(n1, n2):
            s1, s2 = find(n1), find(n2)
            if s1 != s2:
                par[s1] = s2
            else:
                res.append([n1, n2])
        
        res = []
        for x, y in edges:
            # print(x, y)
            union(x, y)
        # return res
        # print(res)
        return res[-1]
