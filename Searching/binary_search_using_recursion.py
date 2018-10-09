#Binary search using recursion
#Eg: [2,3,5,7,9,12,15,17]
#Find 5, 4
def binary_search_helper(arr,low,high,num):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == num:
        return True
    if arr[mid] > num:
        return binary_search_helper(arr,low, mid-1, num)
    else:
        return binary_search_helper(arr,mid+1, high, num)

def binary_search(arr,num):
    low = 0
    high = len(arr) - 1
    result = binary_search_helper(arr, low, high, num)
    return(result)

arr = [2,3,5,7,9,12,15,17]
print(binary_search(arr,2))