
# Top-down (Recursive)

def merge(left, right):
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left
    
    result = []
    i = j = 0

    while len(result) < len(left) + len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i == len(left):
        result += right[j:] # result.extend(right[j:])
    
    if j == len(right):
        result += left[i:]
    
    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))



# Bottom-up (Iterative)

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = a[l + i]
    for i in range(n2):
        R[i] = a[m + i + 1]
    
    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        
        k += 1
    
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def mergeSort(a):

    current_size = 1
    while current_size < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            mid = min(left + current_size - 1, len(a) - 1)
            right = min(2 * current_size + left - 1, len(a) - 1)

            merge(a, left, mid, right)
            left += current_size*2
        
        current_size *= 2







