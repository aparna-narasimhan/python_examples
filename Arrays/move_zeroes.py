'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative orderof the non-zero elements.
Eg: I/P: [0,1,0,3,12]
    O/P: [1,3,12,0,0]
'''
class Solution:
    def moveZeroes(self, nums):
        i = 0
        length = len(nums)
        count = 0
        while(count < length):
            count += 1
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
            else:
                i += 1
        print(nums)

s = Solution()
s.moveZeroes([1,0,0,3,2,0])