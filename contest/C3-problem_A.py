n = int(input())
 
for i in range(n):
    w = str(input())
    N = len(w)
    if N > 10:
        print(f"{w[0]}{N-2}{w[N-1]}")
    else:
        print(w)
