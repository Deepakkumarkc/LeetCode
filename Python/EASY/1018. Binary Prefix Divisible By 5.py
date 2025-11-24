from typing import *
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        for i in range(len(nums)):
            print ((val << 1))
            val = ((val << 1) + nums[i]) % 5
            nums[i] = val == 0
        return nums


solve = Solution()
nums = [0,1,1]

print(f"Output {solve.prefixesDivBy5(nums)}")