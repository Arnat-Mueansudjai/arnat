class Solution(object):
    def canJump(self, nums):
        max_N = 0
        for i in range(len(nums)):
            if i > max_N:
                return False
            max_N = max(max_N, i + nums[i])
        return True

i = Solution()
nums = [3,2,1,0,4]
print(i.canJump(nums))
