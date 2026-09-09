class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        #this dp represents the fewest number of coins to get to amount

        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        return -1 if dp[-1] == float("inf") else dp[-1]