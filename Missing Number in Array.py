class Solution:
    def missingNumber(self,array,n):
        # code here
        arrsum = sum(array)
        t = (n * (n + 1)) // 2
        return t - arrsum # Question link: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/0
