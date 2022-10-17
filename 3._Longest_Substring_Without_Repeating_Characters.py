class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        technique was sliding windows and two pointers
        were if s[j] not in visited then it will be added if s[j] in visited then we will
        increament i by 1 and update visited by s[i:j] which means not including s[j]
        then calculate the length of the visited everytime and find the max of it
        '''
        i,j = 0, 0 
        t = ""
        m = 0
        while j < len(s):
            if s[j] in t:
                t = s[i:j]
                i += 1
            else:
                t+=s[j]
                j+=1
            m = max(m,len(t))
        return m
        print(m)
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
