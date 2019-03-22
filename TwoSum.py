class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 1:
            return [-1, -1]
        else:
            for i in range(0,len(nums)):
                num1 = nums[i]
                temp_list = nums[i+1:]
                j = target - num1
                if j in temp_list:
                    return [i,temp_list.index(j)+i+1]
