class Solution:
    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        print (f"length: {length}")
        for i in range(length):
            print (f"range value: {s[i]}")
            
            if s[i] == "0":                
                total += consecutive * (consecutive + 1) // 2
                print (f"total: {total} : consecutive: {consecutive}")
                consecutive = 0
            else:
                consecutive += 1
            print (f"total: {total} : consecutive: {consecutive}")

        total += consecutive * (consecutive + 1) // 2
        print (f"total: {total}")
        total %= 10**9 + 7
        print (f"total: {total}")
        return total

s = "0110111"    
solver = Solution()
print(solver.numSub(s)) 
