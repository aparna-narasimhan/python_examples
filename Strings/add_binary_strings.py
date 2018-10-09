'''
Add binary strings
"1000","10" -> "1010"
'''
def add(A,B):
    #Convert the given numbers to decimal
    #Add the numbers
    #Convert number to decimal
    #Return the number
    num_A = atoi(A)
    num_B = atoi(B)
    print("num_A", num_A)
    print("num_B", num_B)
    dec_A = bin_to_dec(num_A)
    dec_B = bin_to_dec(num_B)
    print("dec_A", dec_A)
    print("dec_B", dec_B)
    result = dec_to_bin(dec_A+dec_B)
    print(result)

def bin_to_dec(num):
    pow = 0
    res = 0
    while num > 0:
        digit = num % 10
        res += digit * (2 ** pow)
        pow += 1
        num = num // 10
    return res

def dec_to_bin(num):
    stack = []
    res = ""
    while num > 0:
        rem = num % 2
        stack.append(rem)
        num = num // 2
    print("stack", stack)
    while len(stack) > 0:
        res += str(stack.pop())
    return res

def atoi(s):
    #Use a dictionary
    atoi_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}
    result = 0
    for ch in s:
        result = result * 10 + atoi_dict[ch]
    #print(result)
    return(result)

add("1000","10")