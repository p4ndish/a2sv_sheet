class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        a = b = 0
        
        while a < len(word1) and b < len(word2):
            res += word1[a]
            res += word2[b]
            a += 1
            b += 1
        
        if a != len(word1):
            res += word1[a:]
        if b != len(word2):
            res += word2[b:]
        # print(res)
        return res
