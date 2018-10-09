def plusOne(digits):
  idx = len(digits) - 1
  digits[idx] += 1
  if digits[idx] != 10:
    return(digits)
  else:
    while(idx > 0 and digits[idx] == 10 ):
      digits[idx] = 0
      digits[idx-1] += 1
      idx -= 1
    if digits[0] == 10:
      digits[0] = 0
      digits.insert(0,1)
  return(digits)

print(plusOne([2,9,9,1,9]))

class Solution:
    def plusOne(self, A):
        num = 0
        exp = len(A) - 1
        for i in range(len(A)):
            num = num + (A[i] * (10 ** exp))
            exp -= 1
        num += 1
        num_list = self.conv_num_to_list(num)
        return(num_list)

    def conv_num_to_list(self,num):
        result = []
        while(num > 0):
            digit = num % 10
            result.insert(0,digit)
            num = num // 10
        return(result)

s = Solution()
res = s.plusOne([0,9])
print(res)