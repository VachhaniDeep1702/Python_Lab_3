def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

elements = [22, 13, 4, 8, 17, 26, 53, 4]

selection_sort(elements)

print("Sorted elements:", elements)
