class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        if you think dagim, if the arr is sorted and the first element and the last element can't 
        make a pair then there is no way it can pair with the other small elements because it's
        increasing... so if you i and j are less or qual to limit both pointers move to middle 
        else the last element only will have it's own seat 
        '''
        people.sort()
        print(people)
        i = 0
        j = len(people)-1
        c = 0 
        
        while i <= j:
            if people[i] + people[j] <= limit:
                c+=1
                j-=1
                i+=1
            else:
                if people[j] <= limit:
                    c+=1
                    j-=1
                else:
                    j-=1
                
        print(c)
        return c
        
        
        
        
        
        
        
        
        
        
        
