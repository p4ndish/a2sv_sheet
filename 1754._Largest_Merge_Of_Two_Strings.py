class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # return 0
        if word1 and not word2: return 0
​
        m = ""
        while word1 and word2:
            if word1 >= word2:
                m += word1[0] 
                word1 = word1[1:]
            else:
                m += word2[0]
                word2 = word2[1:]
        m += word1
        m+= word2
        return m 
        # m = ""
        # l = r = 0
        # N = len(word1)
        # n = len(word2)
        # while l < N and r < n:
        #     if word1[l] > word2[r]:
        #         m += word1[l]
        #         l += 1
        #     elif word1[l] < word2[r]:
        #         m += word2[r]
        #         r += 1
        #     else:
        #         r += 1
        #         l += 1
        # # print(l, r,word2[r:])
        # if l < N : m += word1[l:]
        # if r < n : m += word2[r:]
