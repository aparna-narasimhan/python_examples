def fact(num):
    if(num<0):
        raise "Number cannot be negative!"
    if(num==0):
        return(1)
    return(num*fact(num-1))

res=fact(-7)
print(res)