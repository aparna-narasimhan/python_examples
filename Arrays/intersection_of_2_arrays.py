#This does not find elements common to both arrays if order is different
class Solution:
    def intersect(self, nums1, nums2):
        result = []
        start_idx = -1
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return(result)
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                start_idx = i
                result.append(nums2[0])
                break

        if start_idx >= 0:
            for i in range(1, len(nums2)):
                if start_idx + i < len(nums1) - 1 and nums1[start_idx + i] == nums2[i]:
                    result.append(nums2[i])
                else:
                    break

        return(result)