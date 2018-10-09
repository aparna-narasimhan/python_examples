#Looks like this is O(N) solution. Also it doesn't pass all the test cases in Leetcode. Checkout more efficient 0(log(n)) solutions
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #When n=0, return 1.0
        #When n>0, return x*x n times
        #When n<0, return 1/2^n
        #return float
        if( n > 0 ):
            pow = pow_helper(x, n)
        elif( n < 0 ):
            pow = 1.0 / pow_helper(x, abs(n))
        else:
            pow = 1.0
        return(pow)

def pow_helper(x, n):
    pow = 1.0
    for i in range(n):
        pow = pow * x
    return(pow)