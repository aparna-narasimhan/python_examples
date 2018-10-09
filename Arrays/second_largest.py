def find_second_largest(list):
    max=-500
    for l in list:
	    if l > max:
	        second_max = max
	        max=l
	    else:
	        if l > second_max:
	            second_max=l

    return(max, second_max)

max, second_max = find_second_largest([17,10,1,15,5,14])
print("max is %d and second max is %d" %(max, second_max))