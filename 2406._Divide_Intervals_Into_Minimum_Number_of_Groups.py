class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        prefix = Counter()
        
        for start, end in intervals:
            prefix[start] += 1
            prefix[end+1] -= 1
            
            
        current = 0
        ans = 0 
        print(prefix)
        for i in sorted(prefix.keys()):
            print(prefix[i])
            current += prefix[i]
            ans = max(ans, current)
            
        return ans
        
        
'''
[[5,10],[6,8],[1,5],[2,3],[1,10]]
0 1 2 3 4 5 6 7 8 9 10 11
          1            -1
            1    -1
  1        -1
    1  -1
  1                     -1
0 2 1 0 -1 1 0 0 0 -1 0 -2
0 2 3 3 2 3  3 3 3 2  2  0
'''
