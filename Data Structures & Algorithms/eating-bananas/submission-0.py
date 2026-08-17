class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        max_banana = max(piles)
        mini = -1
        while l <= max_banana:
            mid = (l + max_banana) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                l = mid + 1
            else:
                max_banana = mid - 1
                mini = mid
        return mini