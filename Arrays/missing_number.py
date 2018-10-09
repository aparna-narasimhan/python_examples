'''
If elements are in range of 1 to N, then we can find the missing number is a few ways:
Option 1 #: Convert arr to set, for num from 0 to n+1, find and return the number that does not exist in set.
Converting into set is better for lookup than using original list itself. However, space complexity is also O(N).

Option#2: Sum of all elements from 1 to N - Sum of all elements in the array = Missing number
Adv: No space complexity

Option#3: XOR all elements in the array + XOR all elements from 1 to N = Missing number
Provided no duplicates?
Adv: No space complexity
XOR is fast operation

'''

#[1,2,3,5,6,7,8]
def find_missing_number(arr):
    n = len(arr)
    total_sum = sum(range(1,arr[-1]+1))
    print(total_sum)
    arr_sum = sum(arr)
    print(arr_sum)
    missing_num = total_sum - arr_sum
    print(missing_num)

find_missing_number([1,2,3,5,6,7,8])