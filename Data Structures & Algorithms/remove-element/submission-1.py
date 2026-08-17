class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1


        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            
            elif nums[r] == val:
                r-=1
            
            elif nums[l] != val:
                l+=1
        
        return r + 1