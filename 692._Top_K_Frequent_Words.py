class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
​
        for s in words: #O(n)
            d[s] += 1 
        heap = []
        for key,val in d.items(): #O(n)
            heapq.heappush(heap, (-val, key)) #O(logn)
        # print(heap)
​
        res  = [heapq.heappop(heap)[1] for _ in range(k) ] #O(logn)
        # res.sort()
        # print(res)
        return res
