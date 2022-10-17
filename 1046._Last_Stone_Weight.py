class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if stones else 0
        stones = [-x for x in  stones]
        heapq.heapify(stones)
        
        j = 0
        while j < len(stones):
            if len(stones) <= 1:
                break
            y = -1 * heapq.heappop(stones) 
            x = -1 * heapq.heappop(stones) 
            if y != x :
                y = y-x
                heapq.heappush(stones,-y)
                j+1
            else:
                j+=2
        c = [-1*x for x in stones ]
        # print(c)
        return self.lastStoneWeight(c)
        # return c[0] if not stones else sum(c)
                
