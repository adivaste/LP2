def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if (arr[j] < arr[min_index]):
                min_index = j
        
        if (min_index != i):
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

# Example usage
arr = [12,0,0,0,12,44,-1,-5,0,64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# Algo : Finding the minimum element of given array and put it in
# 0th index, then search in remaining array and put in 1st index and
# so on