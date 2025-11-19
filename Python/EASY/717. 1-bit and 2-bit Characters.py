class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        print(f"Length: {len(bits)}")
        while i < len(bits) - 1:
            print(f"Befor i is {i}")
            i += bits[i] + 1
            print(f"After i is {i}")
        return i == len(bits) - 1
    

bits = [1,1,1,0]
print(f"Output: {Solution().isOneBitCharacter(bits)}")