class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sorter(x,y):
            if x+y > y+x:
                return -1
            elif y+x > x+y:
                return 1
            else:
                return 0
            
        
        ssort = sorted(map(str, nums), key=cmp_to_key(sorter))
        print(ssort)
        return "".join(ssort) if ssort[0] != "0" else "0" 
