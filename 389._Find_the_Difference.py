class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # counting the occurance of s string for a later use
        c = Counter(s)
        for i in t:
            if i not in s: # if the letter in t is not in s that number is added
                return i
            else:
                c[i] += 1
        
        # else we know that if it occurs in s and occurce in t it give us 2,4,6 on 
        #the hashmap soo if odd value return that letter
    
        for k,i in c.items(): 
            if i % 2 != 0 :
                return k
