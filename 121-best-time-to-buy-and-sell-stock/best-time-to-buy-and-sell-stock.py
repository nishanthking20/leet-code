class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=max(prices)
        b=0
        for i in prices:
            a=min(a,i)
            b=max(b,i-a)
        return b