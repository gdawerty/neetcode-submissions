class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[r] < nums[mid]: #pivot is between here
                l = mid + 1
            else:
                r = mid

        return nums[l]