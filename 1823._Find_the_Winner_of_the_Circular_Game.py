class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(n)]
        
        cur = 0
        for _ in range(n - 1):
            # print("current: ", cur)
            cur = (cur + k - 1) % len(players)
            # print("After: ", cur, "\n")
            players.pop(cur)
            
        return players[0] + 1
        
        
        
        
        
        
        
        
