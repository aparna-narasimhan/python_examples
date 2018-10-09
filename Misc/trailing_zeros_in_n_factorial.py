class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        fact = self.factorial(A)
        while(fact % 10 == 0):
            count += 1
            fact = fact / 10
        return(count)

    def factorial(self,A):
        if A < 2:
            return 1
        return(A * self.factorial(A - 1))

s = Solution()
zeroes = s.trailingZeroes(5)
print(zeroes)