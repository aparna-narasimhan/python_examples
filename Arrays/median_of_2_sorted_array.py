class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = self.merge(nums1, nums2)
        print(nums3)
        median = int(len(nums3)/2)
        if(len(nums3)%2 == 0):
            median_even = (nums3[median] + nums3[median-1])/2
            return(float(median_even))
        else:
            return(float(nums3[median]))

    def merge(self, nums1, nums2):
        i,j = 0,0
        result = []
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j+=1

        result += nums1[i:]
        result += nums2[j:]
        return result