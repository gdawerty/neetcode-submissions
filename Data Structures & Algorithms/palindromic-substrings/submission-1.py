class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        total = 0

        def match(l, r):
            count = 0
            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count +=1

            return count

        for i in range(n):
            count = match(i, i)
            total += count
            count = match(i, i + 1)
            total += count

        return total