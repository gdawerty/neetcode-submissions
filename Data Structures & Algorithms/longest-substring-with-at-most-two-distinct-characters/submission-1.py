from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = defaultdict(int)
        j = 0
        max_len = 0

        for i in range(len(s)):
            count[s[i]] += 1

            while len(count) > 2:
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    count.pop(s[j])
                j += 1

            max_len = max(max_len, i - j + 1)

        return max_len
