class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 1

        while i < len(prices):
            if prices[i] > prices[i - 1]:
                val = prices[i] - prices[i - 1]
                res += val
                i += 1
            else:
                i += 1
                
        return res