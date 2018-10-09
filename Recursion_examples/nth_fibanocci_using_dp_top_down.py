memo={}
def calc_nth_fact_dp_bottom_up(n):
    if n<2:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n]=calc_nth_fact_dp_bottom_up(n-1)+calc_nth_fact_dp_bottom_up(n-2)
    return memo[n]
ans=calc_nth_fact_dp_bottom_up(7)
print(ans)