class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        for i in range(len(nums1)):
            if nums1[i] == nums2[0] and nums1[i : i + len(nums2)] == nums2[::]:
                return(True)
        return(False)