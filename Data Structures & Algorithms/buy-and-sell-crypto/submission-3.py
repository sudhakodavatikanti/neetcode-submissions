class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            print(f'i value : {i}')
            for j in range(i+1, len(prices)):
                print(f'j value : {j}')
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit
        