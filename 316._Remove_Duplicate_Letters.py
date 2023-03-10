import collections
​
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # print(dir(collections))
        stack = []
        visited = set()
        c = Counter(s)
        
        for i in range(len(s)):
            if s[i] in visited:
                c[s[i]] -= 1
            else:
                while stack and stack[-1] > s[i] and c[stack[-1]] > 1 and s[i] not in visited:
                    
                    p = stack.pop()
                    c[p] -= 1
                    visited.remove(p)
                
                visited.add(s[i])
                stack.append(s[i])
        print(stack)
        return "".join(stack)
        
        """
        fabcd
        fcbadabacd
          *
        cbad
        acdb
