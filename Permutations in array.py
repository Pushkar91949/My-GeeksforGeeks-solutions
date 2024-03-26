class Solution:
    def isPossible(self,a, b, n, k):
    # Your code goes here
        a.sort()
        b.sort()
        for i in range(n):
            if a[i] + b[n - i - 1] < k:
                return False
        return True
     # Question link: https://www.geeksforgeeks.org/problems/permutations-in-array1747/0
    
