'''
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

See here for more examples:
https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

TODO: This is a working brute force solution. Need to come up with an optimal solution
'''
from collections import defaultdict
def get_shortest_unique_substring(arr, str):
  arr_dict = defaultdict(int)
  max_count = len(arr)
  min_len = 32768
  result = ""
  for c in range(len(str)):
    length = 0
    count = 0
    start = 0
    for char in arr:
      arr_dict[char] = 1
    for i,ch in enumerate(str[c:]):
      if arr_dict[ch] == 1:
        arr_dict[ch] -= 1
        count += 1
        if start == 0:
          start = c
      length += 1
      if count == max_count:
        if length < min_len:
          min_len = length
          result = str[start:start+length]
          #print result
        break
  return result
