#Merge 2 sorted arrays and update the 1st array in place
#Read each element from the two sorted arrays and append the lower one to the end of first list
class Solution:
    def merge( self, nums1, nums2, m, n ):
        i, j = 0, 0
        while( i < m and j < n ):
            if nums1[ i ] <= nums2[ j ]:
                nums1.append( nums1[ i ] )
                i += 1
            else:
                nums1.append( nums2[ j ] )
                j += 1
        nums1 += nums1[ i: m ]
        nums1 +=  nums2[ j: ]
        del nums1[0:m]
        print( nums1 )

s = Solution()
s.merge( [ 2,5,7 ], [1,2,3], 3, 3 )