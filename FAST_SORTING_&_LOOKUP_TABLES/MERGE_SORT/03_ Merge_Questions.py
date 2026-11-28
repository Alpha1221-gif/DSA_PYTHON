# -- // -- -- QUESTION(1) -- -- \\ -- #
'''Given an array arr[], check if it is sorted in ascending order or not. Equal values 
are allowed in an array and two consecutive equal values are considered sorted'''


def sortedarr(arr):
  # Compare each element with the element right before it
  for i in range(1, len(arr)):
    # Equal values are allowed, so only a smaller value breaks ascending order
    if arr[i] < arr[i - 1]:
      return False

  # Return True if no descending pair was found (also handles empty and 1-element lists)
  return True


# -- // -- -- QUESTION(2) -- -- \\ -- #
'''Given a string consisting of lowercase letters, arrange all its letters in ascending order'''

s = "dcba"
result = "".join(sorted(s))
print(result)  # "abcd"

# -- // -- -- QUESTION(3) -- -- \\ -- #
'''Given an n * n matrix mat[][], sort all the elements of the matrix in non-decreasing 
order and return the resulting matrix.'''

def sort_matrix(mat):
    n = len(mat)

    # 1. Flatten the n x n matrix into one list
    flat = [val for row in mat for val in row]

    # 2. Sort all elements in non-decreasing order
    flat.sort()

    # 3. Rebuild the n x n matrix row by row
    return [flat[i * n : (i + 1) * n] for i in range(n)]

mat = [
    [5, 4, 7],
    [1, 3, 8],
    [2, 9, 6],
]

print(sort_matrix(mat))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]