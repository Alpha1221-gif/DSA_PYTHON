# ----CODE1---- #
# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0)
#input : arr[] = [1, 2, 3, 4]
#output : 1 3
class Solution:
    def getAlternates(self, arr):
        result = []
        for i in range(0,len(arr),2):
         result.append(arr[i])
        return result


# ----CODE2---- #
# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
#input : arr[] = [1, 2, 3, 4], x = 3
#output : 2

class Solution:
    def search(self, arr, x):
        # code here
      for i in range(len(arr)):
         if(arr[i]==x):
            return i
        
      return -1



# ----CODE3---- #
# Given an array arr[]. The task is to find the largest element and return it.
#input : arr[] = [1, 8, 7, 56, 90]
#output : 90

class Solution:
    def largest(self, arr):
        # code here
        max_val = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max_val:
                max_val = arr[i]
        return max_val


# ----CODE4---- #
# You are given an array of integers arr[]. You have to reverse the given array.
#input : arr = [1, 4, 3, 2, 6, 5]
#output : [5, 6, 2, 3, 4, 1]

'''CODE1'''
class Solution:
    def reverseArray(self, arr):
        # [:] modifies the original array in-place
        arr[:] = arr[::-1]
        return arr

'''CODE2'''
class Solution:
    def reverseArray(self, arr):
        # .reverse() updates the list directly
        arr.reverse()
        return arr

'''CODE3'''
class Solution:
    def reverseArray(self, arr):
        # Returns a completely new reversed list
        return arr[::-1]


# ----CODE4---- #
# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false
#input : arr[] = [10, 20, 30, 40, 50
#output : true

class Solution:
    def isSorted(self, arr):
        # code here
        if len(arr) <= 1:
            return True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
