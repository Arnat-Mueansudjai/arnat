class Solution(object):
    def hammingWeight(self, n):
        two=[]
        while n>0:
            two.append(n%2)
            n=n//2
        return two.count(1)
        
i=Solution()
print(i.hammingWeight(11))