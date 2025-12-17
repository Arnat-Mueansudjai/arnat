class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        
        i = 1
        while i <= n:
            if i**3 == n:
                return True
            i += 1

        return False

i = Solution()
print(i.isPowerOfThree(27))

            
        