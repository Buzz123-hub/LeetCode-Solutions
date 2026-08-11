class Solution {
    public boolean canPartition(int[] nums) {

        int totalSum = 0;

        // Calculate total sum
        for (int num : nums) {
            totalSum += num;
        }

        // Odd sum cannot be divided equally
        if (totalSum % 2 != 0) {
            return false;
        }

        int target = totalSum / 2;

        // dp[i] = true if we can make sum i
        boolean[] dp = new boolean[target + 1];

        dp[0] = true;

        for (int num : nums) {

            // Traverse backwards
            for (int j = target; j >= num; j--) {

                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
}