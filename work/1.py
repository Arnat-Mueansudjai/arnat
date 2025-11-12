class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    nums[j] = None
       
        nums = sorted((nums))  # เอาค่าซ้ำออก + เรียงลำดับ
        return nums

i = Solution()
nums = [0,0,5,1,1,2,2,3,3,4]
print(i.removeDuplicates(nums))
