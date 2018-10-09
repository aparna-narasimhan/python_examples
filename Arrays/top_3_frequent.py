from collections import defaultdict
class Solution:
    def top3Frequent(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict=defaultdict(int)

        for num in nums:
            nums_dict[num]+=1

        values=nums_dict.values()
        result = self.find_top_3(values)
        print(result)

        result_keys = []
        count = 0
        for res in result:
            for key, val in nums_dict.items():
                if val == res and count < 3:
                    if key not in result_keys:
                        count += 1
                        result_keys.append( key )

        return( result_keys )

    def find_top_3(self, nums):
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
    	return max1,max2,max3

s = Solution()
ans = s.top3Frequent([1,1,1,2,2,3,3,3,3,5])
print(ans)