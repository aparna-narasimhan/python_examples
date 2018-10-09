'''
#1 Convert string to lower case
#2 Iterate through end of string
#3 Skip space and special characters - use is_alpha() or custom implementation
#4 Compare the remaining string is a palindrome
   - use str[::] == str[::-1] - Modify original string or store string without special chars in a separate string
   - Use 2 pointers one at front and 2nd at end and compare both characters and return 0 if doesn't match, else increment front, decrement last and continue comparison and return 1 finally
     - Might have to handle string with odd/even characters in a special way
'''
class Solution:
    def isPalindrome(self, A):
        A = A.lower()
        non_alpha = [' ',':',',']
        j = len(A) - 1
        i = 0
        while i < j:
            if A[i] in non_alpha:
                i += 1
            elif A[j] in non_alpha:
                j -=1
            elif A[i] != A[j]:
                return 0
            else:
                i += 1
                j -= 1
        return 1

s = Solution()
print(s.isPalindrome("A man, a plan, a canal PanAma"))