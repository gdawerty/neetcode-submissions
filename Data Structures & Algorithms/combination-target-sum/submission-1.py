class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0 or index == len(nums):
                return

            path.append(nums[index])
            backtrack(index, remaining - nums[index], path)
            path.pop()

            backtrack(index + 1, remaining, path)

        res = []

        backtrack(0, target, [])
        return res