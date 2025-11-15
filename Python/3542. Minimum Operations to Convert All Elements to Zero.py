from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
        
# --- Test Cases ---

# Example 2: [3, 1, 2, 1]
# Unique values: {1, 2, 3}. 0 is not present. Count: 3.
nums_1 = [3, 1, 2, 1]
Solver_1 = Solution()
print(f"Input: {nums_1}, Output: {Solver_1.minOperations(nums_1)}")
# Expected Output: 3

# Example 1: [0, 2]
# Unique values: {0, 2}. 0 is present. Count - 1: 1.
nums_2 = [0, 2]
Solver_2 = Solution()
print(f"Input: {nums_2}, Output: {Solver_2.minOperations(nums_2)}") 
# Expected Output: 1

# Another case: [1, 1, 1]
# Unique values: {1}. 0 is not present. Count: 1.
nums_3 = [1, 1, 1]
Solver_3 = Solution()
print(f"Input: {nums_3}, Output: {Solver_3.minOperations(nums_3)}") 
# Expected Output: 1