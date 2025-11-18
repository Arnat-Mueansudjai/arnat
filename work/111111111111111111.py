class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = nums=[0]
        for i in range(len(nums)):
                current_sum = max(nums[i],current_sum+nums[i])
                max_sum = max(current_sum ,max_sum) 
                
        if max_sum <0:
            max_sum=nums[0]
        return max_sum


i = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(i.maxSubArray(nums))
