class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        sums = 0
        res = 0
        N = len(grid)
        clen = len(grid[0])
        for idx,row in enumerate(grid):
            # print(row)
            #check wheather it's eligable
            if N - (idx + 1) < 2:
                break
                #calc the 1 and 3 upto 3element
                #[6,2,1]
                #[9,2,8]
            l = 0
            csums = 0
            for r in range(len(row)):
                if (r - l + 1) > 3: 
                    csums -= grid[idx+2][l]
                    csums -= grid[idx][l]
                    # csums -= mid
                    l += 1
                    
                csums += grid[idx+2][r]
                csums += grid[idx][r]
                
                if (r - l + 1) == 3:
                    
                    mid = grid[idx+1][l:r+1][1]
                    # print(mid)
                    res = max(res, csums+mid)
                #find the mid
                # mid = clen // 2
                # csums += grid[idx+1][mid]
        print(res)
        return res
