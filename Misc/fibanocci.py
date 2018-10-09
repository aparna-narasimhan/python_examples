def main():
    num=13
    l=[]
    l=fib(num)
    print l
    return
def fib( num ):
    l=[]
    j=0
    l.insert(0,0)
    while(l[len(l)-1] != num):
        if(j==0):
           j=j+1
           l.insert(j,1)
           j=j+1
        else:
           l.insert(j,l[j-1]+l[j-2])
           j=j+1
    return l
#Call to main    
main()
