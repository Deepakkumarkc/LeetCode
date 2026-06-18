class Solution:
    def countOdds(self, low: int, high: int) -> int:
        print((low // 2))
        return (high + 1) // 2 - (low // 2)
        
low = 3
high = 7
print(f"output {Solution().countOdds(low,high)}")