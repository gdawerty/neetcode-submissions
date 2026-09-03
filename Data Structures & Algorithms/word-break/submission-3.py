class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        

        n = len(s)

        dp = [False] * (n + 1)
        
        #base case

        dp[0] = True


        for i in range(1, n + 1):
            for j in range(i):
                if s[j: i] in wordDict and dp[j]:
                    dp[i] = True
                    break


        return dp[-1]