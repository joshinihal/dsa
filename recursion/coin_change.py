# Coin change (https://en.wikipedia.org/wiki/Change-making_problem)
# Given a target amount n and a list (array) of distinct coin values,
# what's the fewest number of coins needed to make the change amount.
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change.
# With 1 coin being the minimum amount.

# very slow and works only for american coin system (1,5,10,25) and not for 2,7 etc.
def recursive_coin_change(target,coins):
#     set minimum as default
    min_coins = target
#     if an exact coin is found, return it.
    if target in coins:
        return 1

    else:
#   for each in coins which is smaller than target, 
#  subtract the coin value from target and add the coin count in num_coins
        for i in [c for c in coins if c<= target ]:
            num_coins = 1 + recursive_coin_change(target-i,coins)
#             if num coins is less than minimum, save it as minimum.
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins
 
 # takes a long time for this input
 coin_change(63,[1,5,10,25]) 
