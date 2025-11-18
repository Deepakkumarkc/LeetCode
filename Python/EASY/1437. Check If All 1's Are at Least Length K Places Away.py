from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        
        prev = None
        for i, num in enumerate(nums):
            print (f"Enumerate i = {i}, Num = {num}")
            if num == 1:
                print(f"i : {i}")
                print(f"prev : {prev}")
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True

nums = [1,0,0,0,1,0,0,1]
k = 2
solver = Solution()
#result = Solution().minimumOneBitOperations(n) # Creates a temporary instance and calls the method

print(f"Input nums: {nums} ,K value: {k}, Output: {solver.kLengthApart(nums,k)}" )
