from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            print('i= ', i)
            tmp = int(i%3)
            print('tmp= ', tmp)
            ans+=min(tmp,3-tmp)  
            print('ans= ', ans)          
        return ans

nums = [1,2,3,4]    
print(f"Output: {Solution().minimumOperations(nums)}")