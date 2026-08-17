class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        j = 0

        for i in range(n):
            count[s[i]] += 1
            if len(count) > 2:
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    count.pop(s[j])
                j += 1
        return i - j + 1