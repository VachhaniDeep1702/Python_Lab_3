def sequential_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1


elements = [1, 3, 5, 8, 10, 23, 35]
search_element = 4
result = sequential_search(elements, search_element)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print(f"Element not found in the list.")
