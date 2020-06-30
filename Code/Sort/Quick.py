from random import randint

# Extra space

def quicksort(array):
    if len(array) < 2:
        return array
    
    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
        
    return quicksort(low) + same + quicksort(high)

# partition 1

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

# partition 2

def partition(array, start, end): # [start, end]
    pivot = array[start]
    low = start + 1
    high = end

    while 1:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low <= high and array[low] <= pivot:
            low += 1
        
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]


def quickSort(arr, low, high): # [Low, High]
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
