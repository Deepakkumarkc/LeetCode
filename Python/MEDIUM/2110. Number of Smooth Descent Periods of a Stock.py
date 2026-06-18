from typing import *
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 1  
        prev = 1  
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                print(f"prices[{i}] = {prices[i]} == price[{i-1}]-1 == {prices[i - 1] - 1}")
                prev += 1
                print('Prev', prev)
            else:
                print(f"price[{i}] == {prices[i]}")
                prev = 1
                print('Prev', prev)
            res += prev
            print('res', res)  
        return res
    
solve = Solution()
prices = [3,2,1,4]
print(f"Output: {solve.getDescentPeriods(prices)}")