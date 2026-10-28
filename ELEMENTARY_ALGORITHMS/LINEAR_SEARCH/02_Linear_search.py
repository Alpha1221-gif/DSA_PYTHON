#  ---- CODE ----  #

def linear_search(arr,target):
    # 1. Loop through every element in the list one by one

    for i in range(len(arr)):
        # 2. Check if the current element matches the target

        if arr[i] == target:
            # Return the position (index) where it was found

            return i 
    return -1

# --- Example Usage ---
numbers = [10,20,30,40,50,60,70]
search_no = 60

# Call the function
result = linear_search(numbers,search_no)

# Print the final outcome
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")

# Output = Element found at index: 5