#    ---- FOR BUBBLE SORT ----    #

def bubblesort(arr):
    # Check if the list is already sorted
    if arr == sorted(arr):
        # Print message and exit early
        print("Array are already sorted")
        return arr

    # Get total number of items
    n = len(arr)

    # Outer loop for number of passes
    for i in range(n):
        # Inner loop ignores already sorted tail items
        for j in range(0, n - i - 1):
            # If left is smaller than right, swap for descending order
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the descending sorted array
    return arr


# Implementation: test with an unsorted array
data = [2, 5, 1, 4]
result = bubblesort(data)
print("Sorted array:", result)
# OUTPUT = Sorted array: [5, 4, 2, 1]



#    ---- FOR SELECTION SORT ----    #


def selectionsort(arr):
    # Check if the list is already sorted in ascending order
    if arr == sorted(arr):
        # Print status message and return early
        print("Array are already sorted")
        return arr

    # Store the total number of elements in the array
    n = len(arr)

    # Loop through each position except the very last one
    for i in range(n - 1):
        # Assume the current starting element is the minimum
        min_index = i

        # Scan the remaining unsorted part of the array
        for j in range(i + 1, n):
            # Check if a smaller element is found
            if arr[j] > arr[min_index]:
                # Update the index of the new minimum element
                min_index = j

        # Swap the found minimum element with the element at position i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the fully sorted array
    return arr


# Implementation: test with an unsorted list
data = [64, 25, 12, 22, 11]
result = selectionsort(data)
print("Sorted array:", result)

# OUTPUT = Sorted array: [64, 25, 22, 12, 11]



def insertionsort(arr):
    # Check if the list is already sorted in ascending order
    if arr == sorted(arr):
        print("Array are already sorted")
        return arr

    # Iterate through elements starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        current = arr[i]
        # Set pointer to the index of the preceding element
        prev = i - 1

        # Shift elements smaller than current to the right (descending sort)
        while prev >= 0 and arr[prev] < current:
            arr[prev + 1] = arr[prev]
            prev -= 1

        # Insert current element into its correct sorted position
        arr[prev + 1] = current

    # Return the sorted array
    return arr


# Example implementation / usage
if __name__ == "__main__":
    # Test with an unsorted array
    sample_data = [12, 11, 13, 5, 6]
    print("Original array:", sample_data)

    result = insertionsort(sample_data)
    print("Sorted array (descending):", result)

'''Original array: [12, 11, 13, 5, 6]
Sorted array (descending): [13, 12, 11, 6, 5]'''