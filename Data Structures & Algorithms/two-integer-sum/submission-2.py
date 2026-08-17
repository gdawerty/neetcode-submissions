class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            curr = target - nums[i]

            if curr in seen:
                return [seen[curr], i]
            
            seen[nums[i]] = i

        return [-1,-1]
