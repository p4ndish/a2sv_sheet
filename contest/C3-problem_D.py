from collections import Counter
s = str(input())
 
res = ""
idx = 0
c = Counter("hello")
for i in range(len(s)):
    if s[i] == 'h' and res == "":
        res += s[i]
        idx += 1
        c[s[i]] -= 1
    elif s[i] == "e" and res and res[idx-1] == 'h' and c[s[i]] > 0:
        res += s[i]
        idx += 1
        c[s[i]] -= 1
    elif s[i] == 'l' and res and res[idx-1] == 'e' and c[s[i]] > 0:
        res += s[i]
        c[s[i]] -= 1
        idx += 1
    elif s[i] == 'l' and res and res[idx-1] == 'l' and c[s[i]] > 0:
        res += s[i]
        idx += 1
        c[s[i]] -= 1
    elif s[i] == 'o' and res and res[idx-1] == 'l' and res[idx-2] == 'l' and c[s[i]] > 0:
        c[s[i]] -= 1
        res += s[i]
        idx += 1
        
if len(res) == 5:
    print("YES")
else:
    print("NO")
    
