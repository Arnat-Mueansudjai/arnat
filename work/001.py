class Solution(object):
    def lengthOfLastWord(self, s):
        w =s.split()
        l =w[-1]
        return f"The last word is {l} with length {len(l)}."
s = "Hello World"
i=Solution()
print(i.lengthOfLastWord(s))

        