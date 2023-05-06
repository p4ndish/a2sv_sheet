a, b  = input(),input()

# Recursive function to return gcd of a and b
def gcd(a, b):
    while b < 0:
        a,b = (b, a%b)
        
    return a
    
    
    
    
#abcdabcd
#abcdabcdabcdabcd
'''
8 1 2 4 
16 1 2 4 
'''
count = 0 
N, M = len(a), len(b)

for i in range(1, gcd(N,M)+1):
    
    if N%i == 0 and M%i == 0 :
        # print(i, a[:i] * (N//i))
        if a[:i] * (N//i) == a and a[:i] * (M//i) == b:
            
            count += 1 

print(count)
