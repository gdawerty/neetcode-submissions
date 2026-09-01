class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        l = 0
        seen = {}
        
        
        for r in range(len(fruits)):
            if fruits[r] not in seen:
                seen[fruits[r]] = 1
            else:
                seen[fruits[r]] += 1

            while len(seen) > 2:
                seen[fruits[l]] -= 1
                

                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]

                l +=1

            max_len = max(max_len, r - l + 1)

        return max_len

