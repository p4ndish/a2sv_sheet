class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
            
                
        
          
            
            
            
            
            
            
#         i = 0 
#         j = 0
#         c = 0
#         visited = ""
#         while j < len(s):
#             print(visited)
#             if s[j] in visited:
#                 visited=s[i:j]
#                 i+=1
#             if s[j] not in visited:
#                 visited+=s[j]
#                 j+=1
#             if len(visited) > c:
#                 c = len(visited)
                
#         print(c)
#         return c
        
​
