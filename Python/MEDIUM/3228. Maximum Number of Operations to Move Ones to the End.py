class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        res = 0
        for i, c in enumerate(s):
            print(f"I : {i}, C : {c}")
            if c == '1':
                ones += 1
                print("Ones: ",ones)
            elif i > 0 and s[i - 1] == '1':
                print (f"S: [{i-1}]")
                res += ones
                print("res: ",res)
        return res
    
nums_1 = "10011010"
Solver_1 = Solution()
print(f"Input: {nums_1}, Output: {Solver_1.maxOperations(nums_1)}")

