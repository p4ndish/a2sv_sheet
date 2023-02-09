class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxv = 0
        # if len(height)-1 <= 1:
        #     return 1
        while i <j:
            minv = min(i,j)
            if height[i] < height[j]:
                area =height[i] * (j-i)
                # maxv.append(area)
                maxv = max(maxv, area)
                i+=1
            else:
                area = height[j] * (j-i)
                # maxv.append(area)
                maxv  = max(maxv, area)
                j-=1
        print(maxv)
        return maxv
