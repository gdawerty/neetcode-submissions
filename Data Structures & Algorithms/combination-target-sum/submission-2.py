class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(total, idx, curr):
            if total == target:
                res.append(curr.copy())
                return

            if idx == len(nums) or total > target:
                return

            curr.append(nums[idx])
            backtrack(total + nums[idx], idx, curr)
            curr.pop()

            backtrack(total, idx + 1, curr)

            

        backtrack(0, 0, [])
        return res