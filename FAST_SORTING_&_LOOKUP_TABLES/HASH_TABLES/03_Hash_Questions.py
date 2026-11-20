# //---- QUESTION(1) ----// #


'''Given two arrays a[] and b[] of size m and n respectively, check whether b[] is a 
subset of a[]. Both arrays are not sorted, and elements are distinct.'''

def is_subset(a,b):
    set_a = set(a)  # Store elements of a for fast lookup

    for elements in b:
        if elements not in set_a:
            return False # Found an element in b that is missing from a
    return True

# Example usage:
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

print(is_subset(a, b))  # Output: True