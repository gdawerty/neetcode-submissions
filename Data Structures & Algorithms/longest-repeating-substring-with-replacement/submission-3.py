class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        total = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] +=1
            max_freq = max(max_freq, count[s[r]])
            while (r - l + 1) -  max_freq> k:
                count[s[l]] -=1
                l +=1

            total = max(total, r - l + 1)


        return total


