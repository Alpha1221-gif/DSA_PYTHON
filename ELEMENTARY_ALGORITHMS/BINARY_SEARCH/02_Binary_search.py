#  ---- CODE1 ----  # (FOR EVEN ARRAY)

def binary_search(arr,target):
    start = 0
    end = len(arr) - 1

    # Keep searching as long as the search space is valid
    while start <= end:
        # Calculate the middle index
        mid = start + (end - start) // 2

        # Case 1: Target is found
        if arr[mid] == target:
            return mid

        # Case 2: Target is smaller, discard the right half
        elif target < arr[mid]:
            end = mid - 1

        # Case 3: Target is larger, discard the left half
        else:
            start = mid + 1

    # If the loop finishes without finding the target
    return -1

# --- Example Usage ---
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(numbers,target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")

# OUTPUT = Element found at index: 5

#  ---- CODE2 ----  # (FOR ODD ARRAY)
# Logic is all same for even and odd but must use (//)

def binary_search_even(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

# --- Example with an ODD number of elements (5 items) ---
# Indexes:  0   1   2   3   4   
even_arr = [10, 20, 30, 40, 50]
target_value = 50

result = binary_search_even(even_arr, target_value)
print(f"Element found at index: {result}")

# OUTPUT = Element found at index: 4


#  ----  Binary search by using RECURSION  ----  #

def binary_search_recursive(arr,target,start,end):

    # 1. Base case: Not found
    if start > end:
        return -1
    
    # 2. Find middle
    mid = start + (end-start) // 2

    # 3. Found target
    if arr[mid] == target:
        return mid
    
    # 4. Search left side
    elif target < arr[mid]:
       return binary_search_recursive(arr,target,start,mid-1)
    
    # 5. Search right side
    else:
        return binary_search_recursive(arr,target,mid+1,end)

arr = [2,4,6,8,10,12]
target_value = 10

# Always pass 0 for start, and len(arr) - 1 for end
result = binary_search_recursive(arr,target_value,0,len(arr)-1)
print(result) # Output: 4

    
    


