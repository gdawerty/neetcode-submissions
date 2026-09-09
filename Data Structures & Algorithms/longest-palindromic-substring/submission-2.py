class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        n = len(s)
        bestl = 0
        bestr = 0
        

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l, r

            

        for i in range(n):
            l, r = expand(i , i)

            if (r - 1) - (l + 1) > bestr - bestl:
                bestr = r - 1
                bestl = l + 1
            
            l, r = expand(i, i + 1)

            if (r - 1) - (l + 1) > bestr - bestl:
                bestr = r - 1
                bestl = l + 1           

        return s[bestl: bestr + 1]
        
