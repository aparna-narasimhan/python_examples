def calc_nth_fact_rec(n):
    if n<0:
        return calc_nth_fact_rec(-n)
    if n<2:
        return n
    else:
        return(calc_nth_fact_rec(n-1)+calc_nth_fact_rec(n-2))

ans=calc_nth_fact_rec(-6)
print(ans)