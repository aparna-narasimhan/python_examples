class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Search for 1st char in needle in haystack, if that matches, store the position and search for entire word by slicing. If it matches, return position, return -1 is the whole input string is searched and return 0 if needle is empty

        if needle == "":
            return 0
        first_ch = needle[0]
        substr_size = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == first_ch:
                pos = i
                if haystack[pos : pos + substr_size] == needle:
                    return pos

        return(-1)
