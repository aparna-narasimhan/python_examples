def find_nth_fib(n):
    fib=[]
    fib.insert(0,0)
    fib.insert(1,1)
    for i in range(2,n):
        fib.insert(i,fib[i-1]+fib[i-2])
    return fib[n-1]

res=find_nth_fib(9)
print(res)