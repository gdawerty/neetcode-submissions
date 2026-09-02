class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        l, r = 0, n - 1

        while l < r:
            bar = min(heights[l], heights[r])
            curr = bar * (r - l)
            area = max(area, curr)

            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1


        return area



