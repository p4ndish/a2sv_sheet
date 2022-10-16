class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        s = s.split()
        for i in range(0,len(s)-1):
            print(s[i],s[i+1][:-1], end=' ')
#         for j in range(1,10):
#             for i in s.split():
#                 if str(j) in i:
#                         arr.append(i[:-1])
#         return " ".join(arr)
