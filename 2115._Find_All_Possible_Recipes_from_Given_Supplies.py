class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        
        for r, i in zip(recipes, ingredients):
            indegree[r]  = len(i)
            for ing in i:
                graph[ing].append(r)
        
        
        res = []
        q = deque(supplies)
        
        
        # print(q)
        while q:
            p = q.popleft()
            
            if p in recipes:
                res.append(p)
                
            for recipe in graph[p]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0 :
                    q.append(recipe)
        # print(graph)
        return res
                
                
        
