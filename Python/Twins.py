n = int(input())
coins = list(map(int, input().split()))

target_value = sum(coins) / 2

sum_of_coins = 0
quantity_of_coins = 0

for coin in sorted(coins, reverse=True):
    if (sum_of_coins > target_value):
        break
    
    sum_of_coins += coin
    quantity_of_coins += 1

print(quantity_of_coins)