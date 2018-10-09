#Remove duplicates from sorted array
#Eg: Input: arr = [0,0,1,1,1,2,2,3,3,4] Output: Remove duplicates and return length after. In this case return 5
#Options: Use 2 pointers: say i=0, j=i+1 and if arr[i] == arr[j], remove arr[j] and increment j, compare arr[j ]with arr[i] again and repeat if equal. If not equal, set i = j and j = i +1 and return len(arr)
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = i + 1
        while( j < len(nums) ):
            if( nums[i] == nums[j] ):
                del nums[j]
            else:
                i = j
                j += 1

        return( len( nums ) )

s = Solution()
new_len = s.removeDuplicates( [4,4,8,9,9,9,10] )
print(new_len)