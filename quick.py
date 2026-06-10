def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    pivot_val = key(pivot)
    
    left = [x for x in arr if key(x) < pivot_val]
    middle = [x for x in arr if key(x) == pivot_val]
    right = [x for x in arr if key(x) > pivot_val]
    
    return quick_sort(left, key) + middle + quick_sort(right, key)


def solve_tasks(orders):
    print("--- ИСХОДНЫЕ ДАННЫЕ ---")
    for o in orders: print(o)
    print("\n" + "="*40 + "\n")

    res1 = quick_sort(orders, key=lambda x: x["price"])
    print("1. По цене (возрастание):")
    for o in res1: print(o)
    print("-" * 30)

    res2 = quick_sort(orders, key=lambda x: -x["price"])
    print("2. По цене (убывание):")
    for o in res2: print(o)
    print("-" * 30)

    res3_asc = quick_sort(orders, key=lambda x: x["date"])
    res3 = res3_asc[::-1]
    print("3. По дате (от новых к старым):")
    for o in res3: print(o)
    print("-" * 30)

    res4 = quick_sort(orders, key=lambda x: (x["status"], x["price"]))
    print("4. Сначала по статус, затем по цене:")
    for o in res4: print(o)