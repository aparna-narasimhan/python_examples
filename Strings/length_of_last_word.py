class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        al=[]
        al=A.split()
        size=len(al)
        
        return len(al[size-1])

s = Solution();
s.lengthOfLastWord("Hello World")