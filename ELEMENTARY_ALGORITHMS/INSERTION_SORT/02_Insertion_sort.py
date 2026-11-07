#  ----  CODE  ----  #


def insertion_sort(arr):
    # Check if the array is already sorted; if so, return it immediatel
    if arr == sorted(arr):
        print("The Given Array is already Sorted")
        return arr
    
    # Start from the second element as the first element is already sorted
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1
        
        # Move elements of arr[0..i-1] that are greater than current
        # to one position ahead of their current position
        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous -= 1
            
        # Place current in its correct sorted position
        arr[previous + 1] = current
        
    return arr

# Example usage:
if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]
    print("Original array:", numbers)
    
    sorted_numbers = insertion_sort(numbers)
    print("Sorted array:  ", sorted_numbers)

'''Original array: [12, 11, 13, 5, 6]
Sorted array:   [5, 6, 11, 12, 13]'''