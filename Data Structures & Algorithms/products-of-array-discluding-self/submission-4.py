class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1] * (len(nums) + 1) #1 - indexed
        suffix_sum = [1] * (len(nums) + 1) #1 - indexed

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix_sum[i-1] = suffix_sum[i] * nums[i]

        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = suffix_sum[i] * prefix_sum[i]

        return output

        