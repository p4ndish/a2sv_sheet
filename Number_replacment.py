t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    m = {}
    possible = True
    for i in range(n):
        print(f"array i is -> {a[i]}  string -> {s[i]} ")
        if a[i] not in m:
            m[a[i]] = s[i]
        else:
            if m[a[i]] != s[i]:
                possible = False
                break
        print(f"and on the dict -> {m} ")
    if possible:
        print("YES")
    else:
        print("NO")
