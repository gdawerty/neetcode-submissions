class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            curr = min_height * (r - l)
            area = max(curr, area)

            if heights[l] > heights[r]:
                r-=1
            else:
                l +=1

        return area



