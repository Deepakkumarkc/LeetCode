from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        first_price = prices[0]
        dp = [[0, -first_price, first_price] for _ in range(k + 1)]
        print(f"dp: {dp}")
        n = len(prices)
        
        for day in range(1, n):
            print(f"Day: {day}")
            curr_price = prices[day]
            print(f"curr_price: {curr_price}")
            for trans in range(k, 0, -1):
                print(f"trans: {trans}")
                prev_profit = dp[trans - 1][0]
                print(f"prev_profit: {prev_profit}")
                print(f"dp[{trans}][0]: {dp[trans][0]}")
                print(f"dp[{trans}][1]: {dp[trans][1]}")
                print(f"dp[{trans}][2]: {dp[trans][2]}")
                dp[trans][0] = max(dp[trans][0], dp[trans][1] + curr_price, dp[trans][2] - curr_price)
                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)
                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
                print(f"dp: {dp}")
        
        print(f"dp[{k}][0]: {dp[k][0]}")
        return dp[k][0]
    
solve = Solution()
prices = [1,7,9,8,2]
k = 2
print(f"output: {solve.maximumProfit(prices,k)}")
