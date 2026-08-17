class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        l = 0
        total = 0

        count = defaultdict(int)

        for r in range(len(fruits)):
            count[fruits[r]] +=1
            total +=1


            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -=1
                l+=1
                if count[f] == 0:
                    count.pop(f)

            max_len = max(max_len, total)
        
        return max_len

