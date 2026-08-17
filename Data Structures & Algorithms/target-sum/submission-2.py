class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0] * (2 * sum(nums) + 1) for _ in range(len(nums) + 1)]

        dp[0][sum(nums)] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * sum(nums) + 1):
                ways = 0
                if j - nums[i-1] >= 0:
                    ways += dp[i - 1][j - nums[i-1]]
                if j + nums[i-1] < 2 * sum(nums) + 1:
                    ways += dp[i - 1][j + nums[i-1]]
                dp[i][j] = ways

        return dp[-1][sum(nums) + target] if -sum(nums) <= target <= sum(nums) else 0




