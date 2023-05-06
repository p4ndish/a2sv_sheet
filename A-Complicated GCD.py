def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

gcd_result = a
for i in range(a + 1, b + 1):
    gcd_result = gcd(gcd_result, i)
    if gcd_result == 1:
        break

print(gcd_result)
