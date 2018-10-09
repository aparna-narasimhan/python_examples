class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        '''
        1. Sort the array if not already sorted
        2. Swap every pair of elements
        3. Return the new list
        '''
        A.sort()
        i = 0
        while(i < len(A) - 1):
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
            i += 2
        return A

s = Solution()
ans = s.wave([1,3,2,5,4])
print(ans)