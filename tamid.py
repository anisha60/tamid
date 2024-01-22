#CHALLENGE 1: Sorting & Runtime

arr1 = [1, 3, 5, 8]
arr2 = [1, 2, 3]
arr3 = [2, 8, 15, 30]
arr4 = [1, 2, 3]
arr8 = []

#worst case run time of Python sort is O(n*logn)
def sortArrays(arr1, arr2, k):
    return sorted(arr1 + arr2)[:k]

print(sortArrays(arr1, arr2, 5))
print(sortArrays(arr3, arr4, 2))
print(sortArrays(arr1, arr2, 0))
print(sortArrays(arr1, arr8, 10))

#alternate solution with runtime of O(n)
def sortArrays2(arr1, arr2, k):
    n = len(arr1)
    m = len(arr2)
    merged = [None] * (n + m)
    i = j = s = 0
    while i < n or j < m:
        if i == n:
            merged[s] = arr2[j]
            j += 1
            s += 1
        elif j == m:
            merged[s] = arr1[i]
            i += 1
            s += 1
        elif arr1[i] < arr2[j]:
            merged[s] = arr1[i]
            i +=1
            s += 1
        elif arr1[i] > arr2[j]:
            merged[s] = arr2[j]
            j += 1
            s += 1
        else:
            merged[s] = arr1[i]
            merged[s+1] = arr2[j]
            i += 1
            j += 1
            s += 2
    return merged[:k]

print(sortArrays2(arr1, arr2, 5))
print(sortArrays2(arr3, arr4, 2))
print(sortArrays2(arr1, arr2, 0))
print(sortArrays2(arr1, arr8, 10))


        

