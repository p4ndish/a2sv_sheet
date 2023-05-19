
n = int(input())
mat = [[0]*n for _ in range(n)]

for i in range(n) :
    a = list(map(int, input().split()[1:]))
    for j in a:
        mat[i][j-1] = 1


for r in mat:
    print(*r)
