class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0 
        n = len(tickets)
        
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i]:
                    cnt += 1
                    tickets[i] -= 1 
                if tickets[k] == 0 :
                    return cnt
                
        return cnt
