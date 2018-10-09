def is_palindrome(s,i,j):
    s=s.lower()
    if(len(s)%2==1 and i==j):
        return True
    elif len(s)%2==0 and j<i:
        return True
    elif s[i]==s[j]:
        return(is_palindrome(s,i+1,j-1))
    else:
        return False

inp='Step on nO petS'
length=len(inp)-1
res=is_palindrome(inp,0,length)
print(res)