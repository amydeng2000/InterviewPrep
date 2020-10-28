def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    if amount % max(coins) == 0:
        return amount // max(coins)
    while coins:
        largest = max(coins)
        coins.remove(largest)
        num = amount // largest
        while num >= 0:
            new_amount = amount - num * largest
            flag = coinChange(coins, new_amount)
            if flag >= 0:
                return flag
    return -1



#     return helper(coins, amount)
        
# def helper(coins, amount):
#     if amount == 0:
#         return 0
#     if len(coins) == 0:
#         return -1
#     if amount % max(coins) == 0:
#         return amount // max(coins)
#     largest = max(coins)
#     temp = coins[:]
#     num = amount // largest
#     while num >= 0:
#         print("num = {0}".format(num))
#         new_amount = amount - num * largest
#         print("new_amount = {0}".format(new_amount))
#         flag = helper(coins, new_amount)
#         if flag >= 0:
#             return flag + num
#         num -= 1
#         coins = temp
#     return -1

print(coinChange([186,419,83,408], 6249))