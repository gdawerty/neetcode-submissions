class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        max_prod = 1
        min_prod = 1

        for num in nums:
            
            temp = max_prod * num
            
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp, min_prod * num)

            res = max(res, max_prod)

        return res