# Coin change (https://en.wikipedia.org/wiki/Change-making_problem)
# Given a target amount n and a list (array) of distinct coin values,
# what's the fewest number of coins needed to make the change amount.
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change.
# With 1 coin being the minimum amount.

# very slow and works only for american coin system (1,5,10,25) and not for 2,7 etc.
# def recursive_coin_change(target,coins):
# #     set minimum as default
#     min_coins = target
# #     if an exact coin is found, return it.
#     if target in coins:
#         return 1

#     else:
# #   for each in coins which is smaller than target, 
# #  subtract the coin value from target and add the coin count in num_coins
#         for i in [c for c in coins if c<= target ]:
#             num_coins = 1 + recursive_coin_change(target-i,coins)
# #             if num coins is less than minimum, save it as minimum.
#             if num_coins < min_coins:
#                 min_coins = num_coins
#     return min_coins
 
 # takes a long time for this input
 # coin_change(63,[1,5,10,25]) 
    
 # dynamic programming implementation of above recursive solution is faster 
# as it saves values for certain results instead if calculating them again everytime
def recursive_coin_change_dynamic(target,coins,known_results):
#     set default value for min_coins
    min_coins = target
    
#     if exact coin is found, set it in array as 1 adn return 1
    if target in coins:
        known_results[target] = 1
        return 1
    
#     if coin change is found for a particular target and is greater than 0,
#  return the count of coins
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
#             recursively find the change count for each, add count of 1 to num coins,
#             and subtract the value from target
            num_coins = 1 + recursive_coin_change_dynamic(target-i,coins,known_results)
            if num_coins < min_coins:
                min_coins = num_coins
#                 add to array for particular coin value
                known_results[target] = min_coins
    return min_coins

target = 63
coins = [1,5,10,25]
known_results = [0]*(target+1)
recursive_coin_change_dynamic(target,coins,known_results)
