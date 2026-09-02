class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        total = 0
        l = 0

        for r in range(len(s)):
            

            while s[r] in seen:
                seen.remove(s[l])
                l +=1


            seen.add(s[r])
            total = max(total, len(seen))
            


        return total
