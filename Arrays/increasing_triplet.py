#Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#Eg: [12,11,10,5,6,2,30] -> True(5,6,30)
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False