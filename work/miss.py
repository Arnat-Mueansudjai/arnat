class Solution(object):
    def missingNumber(self, nums):
        max_n=max(nums)
        for i in range(max_n):
            if i not in nums:
                return i
nums =[3,0,1]
i = Solution()
print(i.missingNumber(nums))

