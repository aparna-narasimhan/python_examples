'''
Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
'''
def segregate_arr(arr):
    length = len(arr)
    count = 0
    i = 0
    while count < len(arr):
        count +=1
        print(count)
        if arr[i] < 0:
            i += 1
        else:
            arr.append(arr[i])
            print(arr)
            del(arr[i])
            print(arr)
    print(arr)

segregate_arr([12,11,-13,-5,6,-7,5,-3,-6])