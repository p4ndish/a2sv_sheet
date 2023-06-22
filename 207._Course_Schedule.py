class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        dep = defaultdict(int)
        
        #build the graph 
        for course, pre in prerequisites:
            graph[course].append(pre)
            dep[pre] += 1 
            
        
        q = deque()
        res = []
        #check which node doesn't have incoming edge 
        for i in range(numCourses):
            if dep[i] == 0 :
                q.append(i)
        
        
        while q:
            p = q.popleft()
            res.append(p)
            for neighbours in graph[p]:
                dep[neighbours] -= 1 
                if dep[neighbours] == 0:
                    q.append(neighbours)
        # print(res)
        return True if len(res) == numCourses else False
