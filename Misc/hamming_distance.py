'''
#1: Need a function to calculate hamming distance between 2 numbers - DO XOR of each pair of 2 numbers. The number of 1's in the XOR result will give the hamming distance between those 2 numbers.
#2: find the sum of the hamming distances between all combinations of numbers - Figure out a way to use the already calculated hamming value for (4,2) given (2,4)
#3: Return the sum - modulo?
'''
from collections import defaultdict
ham_dict = defaultdict(int)
class Solution:
    def hammingDistance(self, A):
        ham_dist = 0
        for i in A:
            for j in A:
                ham_dist += self.calc_ham_dist(i ,j)

        return(ham_dist)

    def calc_ham_dist(self,num1, num2):
        if num1 > num2:
            num1, num2 = num2, num1
        if ham_dict[(num1, num2)] > 0:
            return ham_dict[(num1, num2)]
        else:
            result = num1 ^ num2
            count = 0
            while(result > 0):
                if result & 1 == 1:
                    count += 1
                result = result >> 1
            ham_dict[(num1, num2)] = count
            return ham_dict[(num1, num2)]

s = Solution()
print(s.hammingDistance([2,4,6]))