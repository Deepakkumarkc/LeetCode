from typing import *
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        print (sum(nums) % p)
        if sum(nums) % p == 0:
            return 0
        
        sorted_list = sorted(nums)
        remaining = sum(nums) % p  
        count = 0   
        res = 0   

        if remaining in nums:
            return 1

        for i in range (len(sorted_list)):
            print (sorted_list[i])
            if remaining <= sorted_list[i] and res <= res:
                count += 1
                res += i 
                if remaining == res:
                    return count


solve = Solution()
nums = [3,1,4,2]
p = 6
print(f"Output: {solve.minSubarray(nums,p)}")