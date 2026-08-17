class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        max_val = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[l])
                l+=1
            char = s[right]

            if char not in seen:
                seen.add(char)



            max_val = max(max_val, right - l + 1)


        return max_val