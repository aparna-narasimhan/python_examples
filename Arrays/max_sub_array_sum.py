class Solution:
    def maxSubArray(self, nums):
	    #Approach: Set initial sum to 0
		#		   For each element in nums, store sum as the max of current element or current element added to sum
		#          If sum is greater than max_sum, update max_sum to sum
		#		   Return sum
		#Eg: [-2,1,-3,4,-1,2,1,-5,4] => Return 6 => Sum(4,-1,2,1)
		if(len(nums)==0):
			return 0
		sum = 0
		max_sum = nums[0]
		for i in range(len(nums)):
			sum = max(nums[i],nums[i] + sum)
			if sum > max_sum:
				max_sum = sum
		return(max_sum)