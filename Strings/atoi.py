class Solution:
    #Leet code sol
    '''
    Implement atoi which converts a string to an integer.
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
    '''
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        values='0123456789'
        res=0
        found_digit = False
        neg = False
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        for i in range(len(str)):
            if i ==0 and str[i].isalpha():
                return 0
            elif not found_digit and str[i] == '-':
                neg = True
            elif str[i].isdigit():
                found_digit = True
                res = res * 10 + values.index(str[i])
                if res > MAX_INT:
                    if neg:
                        return MIN_INT
                    else:
                        return MAX_INT
            elif found_digit and str[i].isspace() or str[i].isalpha():
                break
        if neg:
            return(0-res)
        else:
            return res

def conv_str_to_int1(string):
values={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
res=0
for s in string:
    res = res * 10 + values[s]
print(res)

def conv_str_to_int1(string):
    values='0123456789'
    res=0
    for s in string:
        res = res * 10 + values.index(s)
    print(type(res))
    print(res)

def conv_str_to_int(string):
    neg = False
    if string[0] == '-':
        neg = True
        string = string[1:]
    result = 0
    for digit in string:
        result *= 10
        for d in '0123456789':
            result += digit > d
            #print(result)
    if neg:
        print( 0 - result)
    else:
        print(result)

conv_str_to_int1("1234")