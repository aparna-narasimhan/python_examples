class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_neg = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif(divisor < 0):
            divisor = -divisor
            is_neg = True
        elif(dividend < 0):
            dividend = -dividend
            is_neg = True

        total = divisor
        quotient = 0
        while(total <= dividend):
            quotient += 1
            total += divisor
        if(is_neg):
            quotient = -quotient
        #return min(max(-2147483648, quotient), 2147483647)
        if quotient >= pow(2, 31)-1 and sign == 1: return pow(2, 31) - 1 #The overflow condition still doesn't seem to work.
        if quotient >= pow(2, 31) and sign == -1: return -pow(2, 31) #This still doesn't seem to work.
        return(quotient)