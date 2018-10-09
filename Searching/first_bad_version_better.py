#First Bad version
class Solution:
    def firstBadVersion(self, n):

        if( n == 0 ):
            return 0
        elif n == 1 and isBadVersion(n):
            return n
        low = 1
        high = n
        mid = ( low + high ) // 2
        while( low <= high ):
            if isBadVersion( mid )
                if not isBadVersion( mid - 1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
            mid = low + high // 2
        return -1