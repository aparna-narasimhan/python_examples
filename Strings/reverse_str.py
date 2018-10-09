class Solution:
    def reverseString(self, s):
        #Approach 1: use s[::-1]
        #return(s[::-1]) #Fastest approach
        #Approach 2: "".join(reversed(s))
        #Approach 3: Strings are immutable in Python, so convert to a list and then convert back to string. This approach is very slow though
        chars = list(s)
        length = len(chars) - 1
        i = 0
        j = length
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)


s = Solution()
print(s.reverseString("hello"))