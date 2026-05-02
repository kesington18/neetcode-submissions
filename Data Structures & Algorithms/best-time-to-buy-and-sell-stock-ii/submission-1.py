class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        i = 1

        while i < len(prices):
            if prices[i] > prices[i - 1]:
                val = prices[i] - prices[i - 1]
                res.append(val)
                i += 1
            else:
                i += 1

        val = sum(res)
        return val