def find_X(arr):
    # Sort the array
    #Apply binary search for each element in the array and do a count of #of elements within the range of X to X+1 and return the element that has the max count
	#TODO: Give negative inputs and check if it works
    arr.sort()
    print(arr)
    max_count = 0
    result = []
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        low = i
        count = 0
        high = len(arr) - 1
        mid = ( low + high ) // 2
        while low <= high:
          if arr[mid] >= ( arr[i] + 1.0 ):
              high = mid - 1
          else:
              count += ( mid - low ) + 1
              low = mid + 1
          mid = (low + high) // 2
        if count > max_count:
            max_count = count
            result = arr[i]
        print("nums b/w {} and {}:{}".format(arr[i],arr[i] + 1.0,count))
    return result

arr = [2.7,3.8,3.9,4.5,4.7,4.8,5.5]
print(find_X(arr))