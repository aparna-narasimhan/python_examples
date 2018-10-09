'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution:
    def countAndSay(self, A):
        result = []
        result.insert(0, "1")
        for i in range(1,A):
            result.insert(i,self.countAndSayHelper(result[i - 1]))
        return(result[A-1])

    def countAndSayHelper(self, num_str):
        count = 1
        i = 0
        res = ""
        while i < len(num_str) - 1:
            if num_str[i] == num_str[i + 1]:
                count += 1
            else:
                res += str(count)
                res += num_str[i]
                count = 1
            i += 1

        res += str(count)
        res += num_str[-1]
        return res

s = Solution()
print(s.countAndSay(5))