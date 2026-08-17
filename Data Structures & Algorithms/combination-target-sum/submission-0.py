class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def backtrack(i, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            
            elif i == len(nums) or remaining < 0:
                return

            else:
                if nums[i] <= remaining:
                    path.append(nums[i])
                    backtrack(i, remaining - nums[i], path)
                    path.pop()
                backtrack(i+1, remaining, path)

        backtrack(0, target, [])

        return res