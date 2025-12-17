class Solution(object):
    def singleNumber(self, nums):
        x=0
        for i in nums:
            x^=i
        return x
       # if nums.count(i) == 1:
        #    return i
nums=[2,2,1]
i=Solution()
print(i.singleNumber(nums))
