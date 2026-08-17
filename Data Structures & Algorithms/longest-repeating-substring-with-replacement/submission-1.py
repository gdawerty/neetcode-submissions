class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_count = 0   # max frequency of a single char in current window
        longest = 0

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] +=1
            max_count = max(max_count, freq[s[right]])

            if (right - left +1) - max_count > k:

                while (right - left+1) - max_count > k:
                    freq[s[left]]-=1
                    left+=1
            longest = max(longest, right - left + 1)

        return longest
