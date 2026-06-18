from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        print('Output: ',(~sum(nums) & 1))
        return (len(nums) - 1) * (~sum(nums) & 1)
    
solve = Solution()
nums = [10,10,3,7,6]
print(f'output: {solve.countPartitions(nums)}')