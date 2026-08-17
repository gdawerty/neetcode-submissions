class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            mid = numbers[l] + numbers[r]
            

            if mid == target:
                return [l + 1, r + 1]
            elif mid < target:
                l+=1
            else:
                r-=1

        return [-1,-1]