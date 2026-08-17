class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = [0] * (len(prices))
        hold = [0] * (len(prices))
        rest = [0] * (len(prices))
        hold[0] = -prices[0]

        for i in range(1,len(prices)):
            sold[i] = hold[i-1] + prices[i]
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            rest[i] = max(rest[i-1], sold[i-1])



        return max(sold[-1], rest[-1], hold[-1])