class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxsum = -float("inf")
        currsum = 0
        for i in range(len(arr)):
            currsum += arr[i]
            maxsum = max(maxsum,currsum)
            
            if currsum < 0:
                currsum = 0
        return maxsum # Question link: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/0
