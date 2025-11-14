class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

x = 10
sol = Solution()
print(sol.mySqrt(x)) 
