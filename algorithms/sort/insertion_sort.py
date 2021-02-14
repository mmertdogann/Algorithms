def insertion_sort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i - 1

        while j >= 0 and key < arr[j]: 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  

arr = [7, 18, 33, 2, 5, 1, 81] 

insertion_sort(arr)                  # Worst case:     O(n^2)
                                    # Best case:      O(n)

print(arr)