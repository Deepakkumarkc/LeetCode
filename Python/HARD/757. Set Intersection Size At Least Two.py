from typing import *
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        print('Intervals     ', intervals)
        intervals.sort(key=lambda x: (x[1], -x[0]))
        print('Sort Intervals', intervals)
        ans = 0
        a, b = -1, -1

        for l, r in intervals:
            print(f"L = {l}, R = {r}")
            print(f"b = {b}")
            if l > b:
                a = r - 1
                b = r
                ans += 2
                print(f"A = {a}, B = {b}, ANS = {ans}")
            elif l > a:
                a = b
                b = r
                ans += 1
                print(f"A = {a}, B = {b}, ANS = {ans}")

        return ans
    
solve = Solution()
intervals = [[1,3],[1,4],[2,5],[3,5]]

print(f"Output: {solve.intersectionSizeTwo(intervals)}")