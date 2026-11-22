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


# //---- QUESTION(2) ----// #
'''Given two arrays a[] and b[], check if they are disjoint, i.e., 
there is no element common between both the arrays.'''

def are_disjoint(a, b):
    set_a = set(a)
    for element in b:
        if element in set_a:
            return False  # Common element found -> not disjoint
    return True       # No common elements -> disjoint

# Example usage:
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

print(are_disjoint(a, b))  # Output: False


# //---- QUESTION(3) ----// #
''''Given two arrays a[] and b[] of equal size, the task is to find whether the
 given arrays are permutation of each other.'''

from collections import Counter


def are_permutations(a, b):
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)

# Example usage:
print(are_permutations([1, 2, 3], [3, 1, 2]))  # True
print(are_permutations([1, 1, 2], [1, 2, 2]))  # False (counts differ)
print(are_permutations([1, 2, 2], [2, 1, 2]))  # True

# //---- QUESTION(4) ----// #
'''Given an integer n, for every positive integer i <= n, the task is to print,

"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3,
"Buzz" if i is divisible by 5
"i" as a string, if none of the conditions are true.'''


def fizz_buzz(n):
    # Store each result item in a list
    result = []

    # Loop through every positive integer i from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check divisibility by both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Check if divisible only by 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Check if divisible only by 5
        elif i % 5 == 0:
            result.append("Buzz")
        # Otherwise store i as a string
        else:
            result.append(str(i))

    # Join all items with ", " and print on a single line
    print(", ".join(result))


# Example call
fizz_buzz(15)
#OUTPUT = 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz


# //---- QUESTION(5) ----// #
'''Given an array arr[], the task is to find the maximum distance between two occurrences 
of any element. If no element occurs twice, return 0.'''

def max_distance(arr):
    # Dictionary to store the FIRST index where each element appears
    first_seen = {}
    
    # Tracks the largest distance found so far (defaults to 0 if no repeats)
    max_dist = 0

    # Loop through the array with both index (i) and value (val)
    for i, val in enumerate(arr):
        if val not in first_seen:
            # First time seeing this element: record its starting index
            first_seen[val] = i
        else:
            # Seen before: calculate distance from its first occurrence to now
            dist = i - first_seen[val]
            
            # Update max_dist if this distance is larger
            if dist > max_dist:
                max_dist = dist

    return max_dist 

# //---- QUESTION(6) ----// #
'''Given an array of integers, arr[] and an integer k, check whether there exist two distinct 
indices i and j such that arr[i] = arr[j] and the absolute difference between their indices is at most k.'''


def contains_nearby_duplicate(arr, k):
    # Edge case: if k is negative, no valid distance can be <= k
    if k < 0:
        return False

    # Stores the MOST RECENT index where each element was seen
    last_seen = {}

    for i, val in enumerate(arr):
        # Check if we've seen this value before and it's within distance k
        if val in last_seen and (i - last_seen[val]) <= k:
            return True

        # Update with the latest index for future comparisons
        last_seen[val] = i

    # No matching pair found within distance k
    return False

# //---- QUESTION(7) ----// #
'''Given two arrays a[] and b[], find their intersection — the unique elements that 
appear in both. Ignore duplicates, and the result can be in any order.'''


def intersection(a, b):
    # Convert both arrays to sets to remove duplicates and allow O(1) lookups
    set_a = set(a)
    set_b = set(b)

    # Find elements present in both sets and return as a list
    return list(set_a & set_b)

# //---- QUESTION(8) ----// #
'''Given two arrays a[] and b[], return the union of both arrays in any order.
The union of two arrays contains all distinct elements that are present in either array.'''

def union_arrays(a, b):
    # Create a set from 'a' to store its unique elements
    union_set = set(a)

    # Add every element from 'b'; duplicates are automatically ignored
    for val in b:
        union_set.add(val)

    # Return the distinct elements as a list (any order is valid)
    return list(union_set)


# //---- QUESTION(9) ----// #
'''Given an integer array arr[], find the element that appears most frequently. If multiple elements 
have the same highest frequency, return the largest among them.'''

def most_frequent_largest(arr):
    # Dictionary to store how many times each element appears
    freq = {}
    for val in arr:
        # Increment count for 'val' (defaulting to 0 if not seen yet)
        freq[val] = freq.get(val, 0) + 1

    # Track the best element found so far and its frequency
    best_val = None
    max_freq = 0

    # Check each unique element and its count
    for val, count in freq.items():
        # Pick 'val' if it appears more often, or ties in frequency and is larger
        if count > max_freq or (count == max_freq and val > best_val):
            max_freq = count
            best_val = val

    # Return the winning element (or None if arr is empty)
    return best_val


# //---- QUESTION(10) ----// #
'''Given an array arr[] of n integers and a target value, check if there
 exists a pair whose sum equals the target.'''


def has_pair_with_sum(arr, target):
    # Stores elements seen so far for fast O(1) lookup
    seen = set()

    for num in arr:
        # The complement needed to reach 'target'
        needed = target - num

        # If the partner number was already seen, a valid pair exists
        if needed in seen:
            return True

        # Record current number for future pairs
        seen.add(num)

    # No pair found
    return False