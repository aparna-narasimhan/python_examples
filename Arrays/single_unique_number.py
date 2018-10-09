#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Best approach with linear time complexity and constant space is to do XOR of the values in the nums. Since every number except for one occurs twice, each                  duplicate pair when XORed gives 0 and hence we are left with the single non-              duplicate number.
        result = nums[0]
        for i in range(1,len(nums)):
            result = result ^ nums[i]
        return(result)

 #Example:
 #Input: [4,1,2,1,2]
 #Output: 4