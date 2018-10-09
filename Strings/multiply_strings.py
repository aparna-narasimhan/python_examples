'''
Multiply strings
"12","10" -> "120"
'''
result = ""
def multiply(A,B):
    #Convert the given strings to numbers
    #Calculate the product
    #return the product
    num_A = atoi(A)
    num_B = atoi(B)
    result = str(num_A * num_B)
    print(result)

def atoi(s):
    #Use a dictionary
    atoi_str = "0123456789"
    result = 0
    for ch in s:
        result *= 10
        for c in range(len(atoi_str)):
            result += ch > atoi_str[c]
    return(result)
    '''
    atoi_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}
    result = 0
    for ch in s:
        result = result * 10 + atoi_dict[ch]
    '''
    print(result)
    return(result)

multiply("12","10")