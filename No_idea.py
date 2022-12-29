# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = input().split()
# print(N)
arr = input().split()
setA = set(input().split())
setB = set(input().split())

happy = 0
for i in arr:
    if i in setA:
        happy += 1
    elif i in setB:
        happy -= 1

print(happy)
# print(list(arr))
