class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            guess = target - num
            if guess in seen:
                return [seen[guess], i]
            seen[num] = i