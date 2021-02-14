def merge_sorted_arr(arr1, arr2):
    sizeA = len(arr1)
    sizeB = len(arr2)

    if sizeA == 0 or sizeB == 0:
        return arr1 + arr2

    merged_array = []
    i = 0
    j = 0

    while i < sizeA and j < sizeB:

        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        
        elif arr2[j] < arr1[i]:
            merged_array.append(arr2[j])
            j += 1
    
    return merged_array + arr1[i:] + arr2[j:]

arr1 = [1,3,4,6,20]
arr2 = [2,3,4,5,6,9,11,76]

merged_array = merge_sorted_arr(arr1, arr2)

print(merged_array)