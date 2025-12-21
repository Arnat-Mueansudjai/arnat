class Solution(object):
    def majorityElement(self, nums):
        count ={}
        for i in nums:
           count[i]=count.get(i,0)+1
        return max(count,kuy=count.get)
i=Solution()
nums = [2,2,1,1,1,2,2]
print(i.majorityElement(nums))