class Solution(object):
    def isPalindrome(self, x):
       strX=str(x)
       ReX=strX[::-1]
       if strX==ReX:
            return True
       else:
            return False     

i=Solution()
x=121
print(i.isPalindrome(x))