class Solution:

    def allFactors(self, A):
        res=[1]
        limit = (A/2)+1
        for i in range(2, limit ):
            if(A % i == 0):
                res.append(i)
        res.append(A)
        return res

        # @param A : integer
        # @param B : integer
        # @return an integer
    def gcd(self, A, B):
        factors_A = self.allFactors(A)
        factors_B = self.allFactors(B)
        return(max(set(factors_A) & set(factors_B)))

s=Solution();
res=s.gcd(8,12)
print res