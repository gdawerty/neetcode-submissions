class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                start = num
                count = 0
                while start in set_nums:
                    count += 1
                    start = start + 1
                longest = max(longest, count)

        return longest