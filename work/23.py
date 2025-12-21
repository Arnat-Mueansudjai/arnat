class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        
        i = 1
        while i <= n:
            if i == n:
                return True
            i*=2

        return False

i = Solution()
print(i.isPowerOfTwo(27))