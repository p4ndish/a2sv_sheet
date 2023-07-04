class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        degree = defaultdict(int)
        
        for parent, child in edges:
            adj[parent].append(child)
            degree[child] += 1
            
        
        q = deque()
        ans = [set() for i in range(n)]
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
                
                
        while q:
            p = q.popleft()
            
            for child in adj[p]:
                ans[child].add(p)
                ans[child].update(ans[p])
                degree[child] -= 1
                if degree[child] == 0:
                    q.append(child)
        # print(ans)
        return [sorted(x) for x in ans]
