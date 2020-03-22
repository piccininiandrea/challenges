'''
https://www.hackerrank.com/challenges/larrys-array/problem
Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. 
He must determine whether the array can be sorted using the following operation any number of times:
Choose any 3 consecutive indices and rotate their elements in such a way that ABC -> BCA -> CAB -> ABC
On a new line for each test case, print YES if A can be fully sorted. Otherwise, print NO.
'''
def larrysArray(A):
    N = len(A)
    #print(A)
    for i in range(N-2):
        m = min(A[i:N])
        j = A.index(m)
        while i != j:
            first = i if j-i < 2 else j-2
            j = rotate(A,first,j)
            #print(A)
    if A.index(max(A)) == N-1:
        return 'YES'
    else:
        return 'NO'

def rotate(A,f,j):
    if f == j-1:
        tmp = A[j]
        A[j] = A[j+1]
        A[j+1] = A[f]
        A[f] = tmp
    if f == j-2:
        tmp = A[j]
        A[j] = A[j-1]
        A[j-1] = A[f]
        A[f] = tmp
    return f
