class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in matrix:
            arr.extend(i)
        
        heapq.heapify(arr)
        while k > 1:
            heapq.heappop(arr)
            k-=1
        print(arr)
        return arr[0]
        # heapq._heapify_max(arr)
        # f = len(arr)-k
        # while f > 0:
        #     heapq._heappop_max(arr)
        #     f-=1
        # print(arr)  
        # return heapq._heappop_max(arr)
