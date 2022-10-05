class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        l = 0
        N = len(tokens)
        r = N - 1 
        score = 0
        mx = 0
        while l <= r:
            
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                mx = max(mx, score)
                l+=1
            elif score > 0:
                
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        print(score, power)
        return mx        
        
        
        
        
        
        
        
        
        
        
        
        
      
