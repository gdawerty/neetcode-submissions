class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * ( len(nums) * 2)

        for i in range(len(arr)):
            arr[i] = nums[i % len(nums)]


        return arr