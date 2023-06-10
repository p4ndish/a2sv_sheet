class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            x,y = heapq._heappop_max(stones),heapq._heappop_max(stones)
            # print(x,y)
            if x != y :
                heapq.heappush(stones, abs(y-x))
#                 
        # print(stones)
        return stones[0] if stones else 0
        
            
