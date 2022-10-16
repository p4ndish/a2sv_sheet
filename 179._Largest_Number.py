class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums.sort()
        if len(nums) <= 1:
            return "".join(map(str,nums))
        else:
            # def cmp(x,y):
            #     if x+y < y+x:
            #         return 1
            #     else:
            #         return -1
            sotor = sorted(map(str,nums), key=cmp_to_key(lambda x,y: 1 if x+y < y+x else -1))
            if sotor[0] == "0":
                return "0"
            else:
                return "".join(sotor)
                
