'''
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
'''
def find_pairs_with_given_difference(arr, k):
  diff_dict = {}
  output = []
  #Looping through the dict once first and storing the values as it is "diff" -> 1-4 is not same as 4-1. We avoided this step in 2 sum as 1+4 = 4+1
  for i in range(len(arr)):
    diff = arr[i] - k
    diff_dict[diff] = arr[i]

  for i in range(len(arr)):
    if arr[i] in diff_dict.keys():
      output.append([diff_dict[arr[i]], arr[i]])

  return output