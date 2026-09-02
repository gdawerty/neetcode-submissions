class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        total = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] +=1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1

            total = max(total, r - l + 1)


        return total


