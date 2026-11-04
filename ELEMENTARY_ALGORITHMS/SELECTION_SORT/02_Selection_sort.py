#  ----  CODE  ----  #

def selection_sort(arr):
    # Check if the array is already sorted before doing anything
    if arr == sorted(arr):
        print("The array is already sorted! No need to run the loops.")
        return arr

    n = len(arr)
    
    # Outer Loop: Only needs to run up to n - 1 times
    for i in range(n - 1):
        # Assume the current position 'i' holds the smallest number
        min_index = i
        
        # Inner Loop: Find the actual smallest number in the rest of the list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found smallest number with the first number of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# --- RUNNING THE IMPLEMENTATION ---

print("--- Test 1: Passing an already sorted list ---")
sorted_list = [1, 2, 3, 4, 5]
selection_sort(sorted_list)

print("\n--- Test 2: Passing an unsorted list ---")
unsorted_list = [64, 25, 12, 22, 11]
print("Original list:", unsorted_list)
selection_sort(unsorted_list)
print("Result list:  ", unsorted_list)


'''--- Test 1: Passing an already sorted list ---
The array is already sorted! No need to run the loops.

--- Test 2: Passing an unsorted list ---
Original list: [64, 25, 12, 22, 11]
Result list:   [11, 12, 22, 25, 64]'''