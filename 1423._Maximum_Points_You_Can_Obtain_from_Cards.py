class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [1,79,80,1,1,1,200,1]   k= 3
         <---------> 
        then remove j from the right and add l from the left to some variable named sum of the [r:]
        '''
        i,j = 0,len(cardPoints) -k  
        s = sum(cardPoints[j:])
        m = s
        while j < len(cardPoints):
            s-= cardPoints[j]
            s += cardPoints[i]
            m = max(m, s)
            i+=1
            j+=1
        return m
