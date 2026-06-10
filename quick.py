def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    pivot_val = key(pivot)
    
    left = [x for x in arr if key(x) < pivot_val]
    middle = [x for x in arr if key(x) == pivot_val]
    right = [x for x in arr if key(x) > pivot_val]
    
    return quick_sort(left, key) + middle + quick_sort(right, key)
