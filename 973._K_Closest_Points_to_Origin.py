class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return s[:k]
#         from math import sqrt
#         # points = [[3,3],[5,-1],[-2,4]]
#         # k = 2
#         points.sort()
#         has = []
#         s = dict()
#         count = 0
#         for i in points:
#             dis = sqrt((i[0])**2+(i[1])**2)
#             has.append(dis)
#             # print(i)
#             s[str(i)]=has[points.index(i)]
​
​
#         # print(has)
​
#         # s['some']='a'
#         ss = sorted(s.items(), key=lambda x: x[1])
#         # print(list(map(list,ss))[0])
#         res = []
#         for i in range(k):
#             res.append(eval(ss[i][0]))
#         return res
