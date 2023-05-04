class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        prime = [True] * n
        i = 2
        while i*i < n:
            if prime [i] == True:
                # Update all multiples of i to False
                for j in range (i*i, n, i):
                    prime [j] = False
            i += 1
        total = 0
        for i in range (2, n):
            if prime [i] == True:
                total += 1
        return total
