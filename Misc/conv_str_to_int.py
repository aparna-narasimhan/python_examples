def conv_str_to_int(string):
    values={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    res=0
    for s in string:
        res = res * 10 + values[s]
    print(res)

def conv_str_to_int(string):
    result = 0
    for digit in string:
        result *= 10
        for d in '0123456789':
            result += digit > d
            print(result)

    print(result)

conv_str_to_int("1234")