class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
i=Solution()
s="kuyyu"
t="yuuyuk"
print(i.isAnagram(s,t))