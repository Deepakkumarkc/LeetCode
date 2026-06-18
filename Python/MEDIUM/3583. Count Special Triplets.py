from typing import *
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        print ("Mod: ",MOD)
        num_cnt = {}
        num_partial_cnt = {}

        for v in nums:
            print ("Before num_cnt GET: ",num_cnt.get(v, 0))
            num_cnt[v] = num_cnt.get(v, 0) + 1
            print ("num_cnt V: ",num_cnt[v])
            print ("num_cnt GET: ",num_cnt.get(v, 0))
            print ("num_cnt: ",num_cnt)

        ans = 0
        for v in nums:
            target = v * 2
            l_cnt = num_partial_cnt.get(target, 0)
            print ("l_cnt: ",l_cnt)
            num_partial_cnt[v] = num_partial_cnt.get(v, 0) + 1
            print ("num_partial_cntV: ",num_partial_cnt[v])
            print ("num_partial_cnt: ",num_partial_cnt)
            r_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)
            print ("r_cnt: ",r_cnt)
            ans = (ans + l_cnt * r_cnt) % MOD
            print ("ans: ",ans)

        return ans

nums = [37,9,24,12,12,24,52,35]
res = []
solve = Solution()
print(f"Output {solve.specialTriplets(nums)}")