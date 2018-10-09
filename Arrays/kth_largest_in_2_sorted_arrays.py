def kth_largest(arr1, arr2, k):
    #Option1: Merge the 2 sorted arrays and then find the result[size-k]: Time:0(m+n), space=extra list or edit the 1st list
    #Option2: Check the last element of 2 lists and go from there
    if k > len(arr1) + len(arr2):
        raise Exception("k is invalid")
    if len(arr1) == 0 and len(arr2) == 0:
        raise Exception("Both arrays are empty")
    i = len(arr1) - 1
    j = len(arr2) - 1
    count = 1
    while i >=0 and j >=0:
        if arr1[i] > arr2[j]:
            if k == count:
                return arr1[i]
            else:
                i -= 1
                count += 1
        else:
            if k == count:
                return arr2[j]
            else:
                j -= 1
                count += 1

    while i>=0:
        if k == count:
            return arr1[i]
        else:
            count += 1
            i -= 1

    while j>=0:
        if k == count:
            return arr2[j]
        else:
            count += 1
            j -= 1

print(kth_largest([1,4,6],[2,5,7],1))