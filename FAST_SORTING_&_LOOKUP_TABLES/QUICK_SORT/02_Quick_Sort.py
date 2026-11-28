# -- // ----  -- CODE -- ---- \\ -- #

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        # Partition the array and get the pivot's final index
        pivot_index = partition(arr, start, end)

        # Recursively sort elements before and after the pivot
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    # Choose the rightmost element as pivot
    pivot = arr[end]
    i = start - 1  # Pointer for the smaller element

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            # Swap elements directly inside the original array
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct sorted position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# Example usage (sorts the list directly in place)
numbers = [10, 7, 8, 9, 1, 5]
quick_sort(numbers)
print(numbers)  # Output: [1, 5, 7, 8, 9, 10]


