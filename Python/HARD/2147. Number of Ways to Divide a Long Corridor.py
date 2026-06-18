class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        n = len(corridor)

        s = 0
        for x in corridor:
            if x == 'S': s+=1
        
        if not s or s % 2 == 1: return 0

        res = 1
        l = 0

        while l < n:
            r = l
            s = 0
            while r < n and s < 2:
                if corridor[r] == 'S' : s += 1
                r += 1
            print(f'while r',r)
            p = 0
            while r < n and corridor[r] == 'P':
                p += 1
                r += 1
            
            print(f'while1 p',p)
            print(f'while1 r',r)

            if r != n and p: 
                print(f'P', (p + 1))
                print(f'res', res)
                res = (res * (p + 1)) % MOD
                print(f'res', res)

            print(f'r',r)
            l = r

        return res
            

solve = Solution()
corridor = "SSPPSPS"
print(f"Output: {solve.numberOfWays(corridor)}")