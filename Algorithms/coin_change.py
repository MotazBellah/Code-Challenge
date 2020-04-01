# Given a target amount n and a list (array) of distinct coin values, 
# what's the fewest coins needed to make the change amount.

def rec_coin(target,coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for value in [ c for c in coins if c<= target]:
            num_coins = rec_coin(target-value, coins) + 1
            min_coins = min(num_coins, min_coins)
    return min_coins


def rec_coin2(target,coins, output=[], t=0):
    if not target:
        return 0
    if target in coins:
        t += 1
        output.append(target)
        x = len(output)
        # print(t)
        output = []
        # print(len(output))
        return x, t

    for i in sorted(coins, reverse=True):
        if target / i >= 1:
            target -= i
            output.append(i)
            t += 1
            return rec_coin(target, coins, output, t)

    return -1

# print(rec_coin(10, [1,5]))
# print(rec_coin(10, [1,5, 10]))
coins = [1,5,10,25]

print(rec_coin(45, coins))
print(rec_coin(23, coins))
print(rec_coin(74, coins))
# print(rec_coin(3, [2]))
# print(rec_coin(0, [1]))
# print(rec_coin(1, [1]))
# print(rec_coin(6249, [186,419,83,408]))
