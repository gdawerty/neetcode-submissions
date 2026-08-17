class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        steps = 0
        l = 0

        while goal > 0:
            for j in range(goal):
                if j + nums[j] >= goal:
                    goal = j
                    steps +=1
                    break

        return steps

            
