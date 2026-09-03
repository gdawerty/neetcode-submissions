class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob this house, skip the next one
        #skip this house, rob the next one
        #take the max of either

        #dp[i] represents the maximum amount of money you get robbing houses up to house i

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        print(dp)

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)
        return dp[-1]