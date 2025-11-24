import typing
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        print(f"Length: {n}, First = {first}, Last = {last}")

        for i, ch in enumerate(s):            
            c = ord(ch) - ord('a')
            print(f"C = {c}, Ord = {ord(ch)} - {ord('a')}")
            if first[c] == -1:
                first[c] = i
            last[c] = i
            print(f"C = {c}, First(c) = {first[c]}, Last(c) = {last[c]}")

        ans = 0
        for c in range(26):
            if first[c] != -1 and last[c] - first[c] > 1:
                mask = 0
                for i in range(first[c] + 1, last[c]):
                    mask |= 1 << (ord(s[i]) - ord('a'))
                ans += bin(mask).count("1")

        return ans
    
solve = Solution()
s = "aabca"
print(f"Output: {solve.countPalindromicSubsequence(s)}")