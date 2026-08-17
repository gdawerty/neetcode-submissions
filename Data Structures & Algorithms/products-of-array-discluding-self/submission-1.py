class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lists = [0] * len(nums)
        total = 1
        for i in range(len(nums)):
            for k in range(len(nums)):
                if k == i:
                    continue
                else:
                    total *=nums[k]
            lists[i] = total
            total = 1
        
        return lists


        