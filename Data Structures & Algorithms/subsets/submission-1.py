class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(path: list, index: int):

            res.append(path[:])
                

            for i in range(index, len(nums)):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()
            

                



        helper([], 0)

        return res