# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a,b = input().split()
# print(type(a),b)

gra = defaultdict(list)
for i in range(int(a)):
    inpu = input()
    gra[inpu].append(str(i+1))
    
grb = set() 
for j in range(int(b)):
    inp = gra[input()]
    
    print(*inp) if inp else print(-1)
