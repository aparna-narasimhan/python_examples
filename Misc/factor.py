class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        res=[-1,1]
        limit = (A/2)+1
        for i in range(2, limit ):
            if(A % i == 0):
                res.append(i)
                res.append(-i)
        res.extend([A,-A])
        return res



s=Solution();
res=s.allFactors(6)
res.sort()
print res