#  ----  CODE  ----  #

def bubble_sort(arr):
    # Check if the array is already sorted before doing anything
    if arr == sorted(arr):
        print("The array is already sorted! No need to run the loops.")
        return arr

    n = len(arr)
    # Go through the list multiple times
    for i in range(n):
        for j in range(0, n - 1):
            # If the current item is bigger than the next one, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

# --- RUNNING THE IMPLEMENTATION ---

print("--- Test 1: Passing an already sorted list ---")
sorted_list = [1, 2, 3, 4, 5]
bubble_sort(sorted_list)

print("\n--- Test 2: Passing an unsorted list ---")
unsorted_list = [5, 1, 4, 2, 8]
print("Original list:", unsorted_list)
bubble_sort(unsorted_list)
print("Result list:  ", unsorted_list)


'''--- Test 1: Passing an already sorted list ---
The array is already sorted! No need to run the loops.

--- Test 2: Passing an unsorted list ---
Original list: [5, 1, 4, 2, 8]
Result list:   [1, 2, 4, 5, 8]'''
