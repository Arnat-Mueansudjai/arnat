class Solution(object):
    def findTheDifference(self, s, t):
        s = s.upper()
        t = t.upper()

        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return t[0]

i = Solution()
print(i.findTheDifference("Yaimak", "yaimakmak"))
