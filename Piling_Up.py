# Enter your code here. Read input from STDIN. Print output to STDOUT
def check(arr):
    l,r = 0,len(arr)-1
    res = float("inf")
    while l < r:
        if arr[r] > arr[l] and arr[r] <= res:
            # print("No")
            res = arr[r]
            r-=1
        elif arr[r] <= arr[l] and arr[l] <= res:
            
            res = arr[l]
            l += 1
        
        else:
            return "No"
    return "Yes"

T = int(input())
# print(T)
for i in range(T):
    n = input()
    arr =list(map(int, input().split()))
    # print(arr)
    print(check(arr))
