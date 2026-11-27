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

''''''
