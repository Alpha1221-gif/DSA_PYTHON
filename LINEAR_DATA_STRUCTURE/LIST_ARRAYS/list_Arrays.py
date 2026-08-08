# ----CODE1---- #
# Given an array (or list), reverse its elements in-place without using extra space for another list.

def reverse_string(arr):
    left = 0
    right = len(arr) - 1

    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr
arr_ = [23,45,67,89,90]
print(reverse_string(arr_))
#output = [90, 89, 67, 45, 23]


# ----CODE2---- #
# Given an array of numbers, return the largest , Smallest value

array = [23,45,67,89,90,31,56,83]

max_num = array[0]
min_num = array[0]
for i in array:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(max_num)  #output = 90
print(min_num)  #output = 23


# ----CODE3---- #
# Remove duplicates from a sorted array so that each element appears only once.

def remove_duplicate(nums):
    if not nums:
        return 0
    
    unique_index = 0
    seen = set()

    for i in range(len(nums)):
        if nums[i] not in seen:
           seen.add(nums[i])
           nums[unique_index] = nums[i]
           unique_index += 1
    return unique_index 

arr = [1,2,3,2,4,2,1,5]
length = remove_duplicate(arr)
print(arr[:length])
#output = [1, 2, 3, 4, 5]


