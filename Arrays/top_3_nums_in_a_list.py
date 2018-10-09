def find_top_3(nums):
	max1,max2,max3 = float("-inf"),float("-inf"),float("-inf")
	for i in range(len(nums)):
		if nums[i] > max1:
			max3 = max2
			max2 = max1
			max1 = nums[i]
		elif nums[i] > max2:
			max3 = max2
			max2 = nums[i]
		elif nums[i] > max3:
			max3 = nums[i]
	return [max1,max2,max3]

max1,max2,max3 = find_top_3([15,5,2,10,3,14,8,17])
print(max1,max2,max3)