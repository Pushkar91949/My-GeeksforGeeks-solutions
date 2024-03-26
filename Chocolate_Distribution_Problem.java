class Solution
{
    public long findMinDiff (ArrayList<Integer> arr, int n, int m)
    {
        int min_diff_final = Integer.MAX_VALUE;

        Collections.sort(arr);

        for (int i = 0; i < n - m + 1; i++) {
            int mini = arr.get(i);
            int maxi = arr.get(i + m - 1);
            int min_diff_curr = maxi - mini;
            if (min_diff_curr < min_diff_final) {
                min_diff_final = min_diff_curr;
            }

        }
        return min_diff_final;
    }
} // Question link: https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/0
