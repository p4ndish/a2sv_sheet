class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i , time in enumerate(tasks):
            time.append(i)
            
        tasks.sort(key=lambda x: x[0])
        res, heap = [], []
        time, t = tasks[0][0], 0 
        N = len(tasks)
        while heap or t < N :
            while t < N and time >= tasks[t][0]:
                heapq.heappush(heap, [tasks[t][1], tasks[t][2]])
                t += 1 
                
            if not heap:
                time = tasks[t][0]
            else:
                p_time, index = heapq.heappop(heap)
                time += p_time
                res.append(index)
        return res
