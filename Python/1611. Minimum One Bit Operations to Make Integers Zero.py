class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        print (ans)
        ans ^= ans >> 16
        print (ans)
        ans ^= ans >> 8
        print (ans)
        ans ^= ans >> 4
        print (ans)
        ans ^= ans >> 2
        print (ans)
        ans ^= ans >> 1
        print (ans)
        return ans


n = 3
solver = Solution()
print(solver.minimumOneBitOperations(n)) 
#print(Solution().minimumOneBitOperations(n))

#--
#solver = Solution()         # Create a named instance (object)
#result = solver.minimumOneBitOperations(n) # Call method on the instance

#--
#result = Solution().minimumOneBitOperations(n) # Creates a temporary instance and calls the method

''' STATIC METHOD

class Solution:
    @staticmethod
    def minimumOneBitOperations(n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans

n = 3
result = Solution.minimumOneBitOperations(n) # Call directly on the class       
'''