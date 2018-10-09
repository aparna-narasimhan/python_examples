'''
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
'''
def max_difference(arr):
    smallest = 0
    max_diff = float('-inf')
    pos1, pos2 = -1, -1
    i = 0
    while(i < len(arr) - 1):
        if arr[i+1] < arr[i]:
            if arr[i+1] < arr[smallest]:
                smallest = i + 1
        else:
            if arr[i+1] - arr[smallest] > max_diff:
                max_diff = arr[i+1] - arr[smallest]
                pos1, pos2 = smallest, i+1
        i += 1
    return(max_diff, pos1, pos2)

max_diff, pos1, pos2 = max_difference([7, 9, 5, 6, 3, 2])
print("Max diff of %d and %d is %d"%(pos1,pos2,max_diff))