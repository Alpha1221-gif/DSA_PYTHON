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