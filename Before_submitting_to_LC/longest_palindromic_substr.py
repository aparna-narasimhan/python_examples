class Solution:
    # @param A : string
    # @return a strings

    def longestPalindrome(self, s):
        length=0
        result=''
        i = 0
        j = len(s) - 1
        for i in range(len(s)):
            for j in range(len(s), i-1, -1):
                sub_str=s[i:j]
                if sub_str==sub_str[::-1]:
                    if(len(sub_str)) > length:
                        length = len(sub_str)
                        #print sub_str
                        result=sub_str
        return result



s=Solution();
str=s.longestPalindrome("babad")
print("result is", str)