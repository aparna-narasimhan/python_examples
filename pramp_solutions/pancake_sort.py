'''
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
'''
# [5,1,4,3,2]
# [2,3,4,1,5] k = 5

# [4,3,2,1,5]
# [1,2,3,4,5] k = 4

# Find index of max
# Bring max to front
# Bring max to the back
# k -= 1

def is_sorted(arr):
  #Check if arr is already sorted
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True

def pancake_sort(arr):
  k = len(arr)
  for i in range(len(arr)):
    #if array is sorted already, just return the sorted arr - Do we need this?
    if is_sorted(arr):
       return arr
    #Find the max num in remaining array
    max_idx = find_max(arr[:k])
    #Take max element and put it in the beginning
    flip(arr, max_idx + 1)
    #Call flip to put the maximum at the end of the remaining array. Now, each element at the end is sorted
    k = len(arr[:k])
    flip(arr, k)
    #decrement k as the last  few elements are already sorted
    k -= 1
  return(arr)

def find_max(arr):
  max = arr[0]
  max_index = 0
  for i in range(1,len(arr)):
    if arr[i] > max:
      max = arr[i]
      max_index = i
  return max_index

def flip(arr, k):
  i = 0
  j = k - 1
  while(i < j):
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
  return arr
