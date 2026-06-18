class Solution:
    def xorAfterQueries(self, nums, queries):
        mod = 1000000007

        # Process each query
        for t in queries:
            l = t[0]
            r = t[1]
            k = t[2]
            v = t[3]
            idx = l
            print(f"l {t[0]}")
            print(f"r {t[1]}")
            print(f"k {t[2]}")
            print(f"v {t[3]}")
            print(f"idx {idx}")


            # Apply operation at step k
            while idx <= r:
                temp = nums[idx]
                print(f"idx {nums[idx]}")
                nums[idx] = (temp * v) % mod
                print(f"nums[idx] {nums[idx]}")
                idx += k

        # Compute XOR of final array
        ans = 0
        for num in nums:
            ans ^= num

        return ans

solve = Solution()

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]

print(solve.xorAfterQueries(nums, queries))