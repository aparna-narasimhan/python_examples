def solve(A):
    count = 0
    if A[::] == A[::-1]:
        return 0
    first = 0
    last = len(A) - 1
    orig_last = len(A)
    while first <= last:
        if A[first] != A[last]:
            A = A[:first] + A[last] + A[first:]
            count += 1
        else:
            last -= 1
        first += 1
        print(A)
        if A[::] == A[::-1]:
            print(A)
            return count
    return count

count = solve("ABC")
print(count)