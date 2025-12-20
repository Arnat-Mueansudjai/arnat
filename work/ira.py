class Solution(object):
    def isSubsequence(self, s, t):
        i = 0 

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
i = Solution()
s = "abc"
t = "ahbgdc"
print(i.isSubsequence(s,t))
