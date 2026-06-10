def quick_sort(arr, key=lambda x: x):
    a = list(arr)
    
    def _quick_sort(left_idx, right_idx):
        if left_idx >= right_idx:
            return
        
        pivot = a[(left_idx + right_idx) // 2]
        pivot_val = key(pivot)
        
        i = left_idx
        j = right_idx
        
        while i <= j:
            while key(a[i]) < pivot_val:
                i += 1
            while key(a[j]) > pivot_val:
                j -= 1
                
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        
        _quick_sort(left_idx, j)
        _quick_sort(i, right_idx)

    _quick_sort(0, len(a) - 1)
    return a
