class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                curr = s[j:i]
                if dp[j] and curr in wordDict:
                    dp[i] = True
        
        return dp[-1]

        