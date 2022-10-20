class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        N = len(citations)
        n = N 
        for i in range(N):
            if n <= citations[i]:
                return n
            
            n -= 1
        return 0
    
        pass
  
