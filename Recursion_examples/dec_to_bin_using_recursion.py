def dec_to_bin(num):
    if num<0:
      dec_to_bin(-num)
    elif num<2:
        print(num)
    else:
        lastDigit=int(num%2)
        restOfDigits=int(num/2)
        dec_to_bin(restOfDigits)
        print(lastDigit)


dec_to_bin(-8)