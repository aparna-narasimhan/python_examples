def main():
    a=[1,2,3,4,5]
    array_left_rotation(a,len(a),2)

def array_left_rotation(a, n, k):
    result=a[k:]+a[:k]
    for r in result:
	    print r;

#------------------------------------------ CALL TO MAIN FUNCTION ----------------------------------------------

main()