#  ----  PROBLEM1  ----  #

'''Given a sorted array arr[] of distinct integers and an integer k, return 
the 0-based index of k if it is present in the array. Otherwise, return -1'''

class Solution:
    def binarySearch(self, arr: list[int], k: int) -> int:
        start = 0
        end = len(arr) - 1
        while start<=end:
            mid = start + (end-start) // 2
            if arr[mid] == k:
                return mid
            elif k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    def search(self,arr: list[int],value) -> int:
        for i in range(len(arr)):
            if arr[i] == value:
                return i
        return -1


#  ----  PROBLEM2  ----  #

'''Given an array arr[], find the elements whose value is equal to the position where they appear.'''

class Solution:
    def valEqualToPos(self, arr:list[int]) -> list[int]:
        result = []
        for i in range(len(arr)):
            if  arr[i] == i :
                 result.append(arr[i])
        return result


#  ----  PROBLEM3  ----  #

'''Given a string s consisting only of '0' and '1', find the last index at which '1' 
occurs. If '1' is not present in the string, return -1.'''

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        return s.rfind('1')


#  ----  PROBLEM4  ----  #

'''Given an array arr[] containing distinct positive integers, and two integers start and end defining a range.
 Find if the array contains all elements within inclusive range [start, end].'''

class Solution:
    def checkElements(self, start, end, arr):
        elements = set(arr)

        for num in range(start, end + 1):
            if num not in elements:
                return False

        return True