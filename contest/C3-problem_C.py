def solve(grid):
    #print(grid)
    for row in range(len(grid)):
        # row = grid[r]
        
        if row == 0: continue
        for col in range(1,len(grid[row])-1):
            if grid[row][col] == "#":
                upL = grid[row-1][col-1]
                upR = grid[row-1][col+1]
                downL = grid[row+1][col-1]
                downR = grid[row+1][col+1]
                if upL == upR == downL == downR == "#":
                    return row+1,col+1
                


test_cases = int(input())
for _ in range(test_cases):
    input()
    grid = [str(input()) for _ in range(8)]
    
    print(*solve(grid))
