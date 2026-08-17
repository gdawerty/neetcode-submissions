class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i - 1]

        print(prefix)

        suffix = [0] * len(nums)
        suffix[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(suffix)

        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = suffix[i] * prefix[i]

        return res