memo = {}
def climbStairs(n):
    global memo
    if n <= 2:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = climbStairs(n-1) + climbStairs(n-2)
        return memo[n]

result = climbStairs(5)
print(result)