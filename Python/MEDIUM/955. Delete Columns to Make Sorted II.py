from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len (strs)
        col = len(strs[0])
        res = 0
        isSorted = [0] * row


        for c in range (col):
            Valid = True
            for r in range (1,row):
                print(f" {strs[r][c]} < {strs[r - 1][c]} and Issorted {isSorted[r]}")
                if not isSorted[r] and strs[r][c] < strs[r - 1][c]:
                    Valid = False 
                    res += 1
                    print ('res:', res)
                    break
            print(f"Valid: {Valid}")           
            if not Valid: continue
            for r in range(1, row):
                print (f"inside for {isSorted}" )
                print(f" test: {strs[r][c]} > {strs[r - 1][c]} and Issorted {isSorted[r]}")
                if strs[r][c] > strs[r-1][c]: isSorted[r] = 1

        return res

solve = Solution()
strs = ["xc","yb","za"]
print(f"Output: {solve.minDeletionSize(strs)}")