result = 0
def coin_change(coins, amount, r=0):
    global result
    max_num = find_max_close_to_num(coins, amount)
    if r == 0:
        result = 0
    rem = amount % max_num
    print("rem", rem)
    if rem == 0:
        result += amount // max_num
        return(result)
    elif rem in set(coins):
        result += (amount // max_num) + rem
        return(result)
    else:
        result += 1
        r += 1
        print("rem", rem)
        return coin_change(coins, rem, r)


def find_max_close_to_num(coins, num):
    max1 = float("-inf")
    for n in coins:
        if n > max1 and n <= num:
            max1 = n
    return(max1)

print(coin_change([1,2,5], 2))