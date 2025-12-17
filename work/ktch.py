class Solution(object):
    def reverseString(self, s):
        l=0
        r =len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

i = Solution()
s = ['h','e','l','o','v','e']
i.reverseString(s)
print(s)
