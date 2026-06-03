class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for left in range(0, len(prices)):
            for right in range(left + 1, len(prices)):
                profit = prices[right] - prices[left]
                print("Left, Right", prices[left], prices[right])
                print("Profit", profit)
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit