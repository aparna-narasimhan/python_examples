'''
Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] < n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Option#1 : Store all numbers as keys and their occurrences as values in a dictionary and return all the keys whose value is 2. However, this has space complexity of O(N)
Option#2 : Choose 1st element and XOR with all other elements one by one and add the number to result when XOR value is 0. However, this takes time complexity of O(N^2)
Option#3: Perform hashing by negating some of the values in the array if +ve and check if its negative next time, add to result. Time complexity: O(N) and space: O(1)
'''

#Option 3 - Can be used even if elements appear how many ever times in the array.
#[4,3,2,7,7,2,3,1]
def find_duplicates(arr):
    result = []
    for i in range(0,len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            result.append(abs(arr[i]))
    return(result)
