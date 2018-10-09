def calc_pow(base,exp):
    if(exp==1):
        return(base)
    else:
        return(base*calc_pow(base,exp-1))

res=calc_pow(9,2)
print(res)