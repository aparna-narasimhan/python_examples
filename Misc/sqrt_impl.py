def find_sqrt(num):
    neg = False
    if(num == 1):
        return float(num)
    if(num < 0):
        neg = True
        num = -num
    start = 0
    end = num
    prev_mid = 0
    precision = 0.00005
    mid = float((start + end) / 2)
    diff = abs(mid - prev_mid)

    while((mid * mid != num) and  (diff > precision)):
        if mid*mid > num:
            end = mid
        else:
            start = mid
        prev_mid = mid
        mid = float((start + end) / 2)
        diff = abs(mid - prev_mid)

    if(neg):
        return(str(mid)+'i')
    else:
        return(mid)

print(find_sqrt(9))

#Time complexity: O(logN)
#Space complexity: O(1)

def sqrt(x):
    last_guess= x/2.0
    print('last guess', last_guess)
    while True:
        guess = (last_guess + x/last_guess)/2
        print('guess', guess)
        print('abs', abs(guess - last_guess))
        diff = abs(guess - last_guess)
        if diff < .000001: # example threshold
            return guess
        last_guess= guess

def estimation_sqrt(x):
  last_guess=x/2.0; # initial estimation
  guess=0; # result
  diff=1.0; # aux. var. for difference in each iteration
  while ( diff > 0.000001 ) :
    guess = (last_guess + x/last_guess)/2
    diff = guess - last_guess
    if (diff < 0):
      diff=-diff
    last_guess = guess
  return guess

res=sqrt(122)
res1=estimation_sqrt(122)
print(res)
print(res1)