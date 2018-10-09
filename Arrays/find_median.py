import math
class Solution:

    def findMedian(self, A):
        sorted_arr = A.sort()
        size = len(A)
        med_idx = int(math.ceil(size/2))
        median = A[med_idx]
        return median

s = Solution()
med = s.findMedian([1,3,5,2,6,9,3,6,9])
print med