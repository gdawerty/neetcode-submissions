class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        print(seen)
        max_val = 0

        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            if curr - 1 not in seen:
                while curr + 1 in seen:
                    count +=1
                    curr +=1

            max_val = max(max_val, count)

        return max_val    