class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        #you can either rob the first house and skip the last
        #or skip the first house and rob the last

        dp_rob1 = [0] * len(nums)
        dp_rob1[0] = nums[0]
        dp_rob1[1] = max(dp_rob1[0], nums[1])

        dp_skip1 = [0] * len(nums)
        dp_skip1[1] = nums[1]

        for i in range(2, len(nums)):
            if i == len(nums) - 1: #skip last house for rob1
                dp_skip1[i] = max(dp_skip1[i-2] + nums[i], dp_skip1[i-1])
            else:
                dp_skip1[i] = max(dp_skip1[i-2] + nums[i], dp_skip1[i-1])
                dp_rob1[i] = max(dp_rob1[i-2] + nums[i], dp_rob1[i-1])

        max1 = max(dp_rob1)
        max2 = max(dp_skip1)
        return max(max1, max2)