n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
 
taken = 0
taken_sum = 0
remaining_sum = sum(coins)
 
for coin in coins:
    taken += 1
    taken_sum += coin
    if taken_sum > remaining_sum - taken_sum:
        print(taken)
        break
