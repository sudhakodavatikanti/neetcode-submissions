class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit , lowest = 0, prices[0]
        for price in prices:
            if price < lowest:
                lowest = price

            if price - lowest > max_profit:
                max_profit = price - lowest

        return max_profit
           

           
        