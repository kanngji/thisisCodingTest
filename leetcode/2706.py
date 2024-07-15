class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        # Check if we can buy at least two chocolates
        if len(prices) < 2 or prices[0] + prices[1] > money:
            return money
        
        # Deduct the cost of the two cheapest chocolates from the money
        money -= prices[0] + prices[1]
        
        return money