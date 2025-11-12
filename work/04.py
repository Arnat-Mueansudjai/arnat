class Solution(object):
    def removeDuplicates(self, nums):
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    nums[j]="_"
        print(nums.sort)
i = Solution()
nums=[0,0,5,1,1,2,2,3,3,4]
print(i.removeDuplicates(nums))

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1