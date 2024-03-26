class Solution:
    def nextPermutation(self, n, arr):
        # code here
        index = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                index = i
                break
        if index == -1:
            arr.reverse()
        
        else:
            for i in range(n-1, index, -1):
                if arr[i] > arr[index]:
                    arr[i], arr[index] = arr[index], arr[i]
                    break
            arr[index+1:] = arr[index+1:][::-1]
        return arr #Question link: https://www.geeksforgeeks.org/problems/next-permutation5226/0
