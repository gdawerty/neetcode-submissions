class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        check = set()
        longest = 0

        for char in s:
            if char not in check:
                curr += char
                check.add(char)
            else:
                # update longest before we shrink
                longest = max(longest, len(curr))
                # shrink from the left until the duplicate is removed
                while char in check:
                    removed = curr[0]
                    curr = curr[1:]
                    check.remove(removed)
                # now safe to add current char
                curr += char
                check.add(char)

            # keep longest up-to-date (handles end-of-string case)
            longest = max(longest, len(curr))

        return longest
