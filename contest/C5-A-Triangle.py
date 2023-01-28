n = int(input())
nums = list(map(int, input().split()))
nums.sort()
 
for i in range(len(nums)-2):
    if nums[i] + nums[i+1] > nums[i+2]:
        print("YES")
        exit()
print("NO")
    
    
