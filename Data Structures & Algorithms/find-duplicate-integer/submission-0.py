class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dups = set()

        for num in nums:
            if num not in dups:
                dups.add(num)
            else:
                return num
        