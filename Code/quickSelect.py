def partition(list, left, right, pivot_index):
    pivot_value = list[pivot_index]
    list[pivot_index], list[left] = list[left], list[pivot_index]
    left += 1

    while 1:
        while left < right and list[left] < pivot_value:
            left += 1
        while left <= right and list[right] >= pivot_value:
            right -= 1
        if left >= right: break
        list[left], list[right] = list[right], list[left]
    
    return right

def select(list, left, right, k):
    if left == right:
        return list[left]
    
    pivot_index = randInt(left, right)

    pivot_index = partition(list, left, right, pivot_index)

    if k == pivot_index:
        return list[k]
    elif k < pivot_index:
        return select(list, left, pivot_index-1, k)
    else:
        return select(list, pivot_index+1, right, k)