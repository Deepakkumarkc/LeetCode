from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int, is_print: str) -> int:

        x = 0
        while x <= len(nums) - 1:

            if is_print == 'Y': print ('x:', x)
            if nums[x] == original:
                original *= 2
                if is_print == 'Y': print ('original:', original)
                x = 0   
            else:
                x += 1      
        return original

    def findFinalValue1(self, nums: List[int], original: int, is_print: str) -> int:
        
        flag = True
        while flag:
            if original in nums:
                original = original * 2
            else:
                return original

solver = Solution()
nums = [5,3,6,1,12]
original = 3

print (f"Nums: {nums} , Originals: {original}")
print(f"findFinalValue function: {solver.findFinalValue(nums, original, 'N')}")
print(f"findFinalValue1 function: {solver.findFinalValue(nums, original, 'N')}")
