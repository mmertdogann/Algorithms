def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


arr = [2, 3, 4, 7, 10, 32, 40, 97]
element = 4

result = binary_search(arr, element, 0, len(arr)-1)               # O(lgN)
 
if result != -1:
    print("Element was found at index: ", str(result))
else:
    print("Element was not found")