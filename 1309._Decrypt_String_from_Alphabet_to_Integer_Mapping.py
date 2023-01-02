class Solution:
    def freqAlphabets(self, s: str) -> str:
        c = defaultdict(str) # getting the corresponding values for the alphabets
        ss = string.ascii_lowercase
        for i in range(26):
            c[str(i+1)] = ss[i]
        res = ""
        i = 0
        #if 12# i have to take 12 instead of 1,2 separetly 
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                res += c[s[i:i+2]]
                i += 2
            else: #else append the single value
                res += c[s[i]]
                i += 1
                
        # print(res)
        return res
