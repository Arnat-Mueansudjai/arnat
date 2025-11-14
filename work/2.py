class Solution(object):
    def plusOne(self, digits):
       d = ""
       for i in range (len (digits)):
            d += str(digits[i])
       num = int(d) + 1
       number = list(map(int, str(num)))
       return number
i =Solution()
digits = [1,2,3]
print(i.plusOne(digits))

