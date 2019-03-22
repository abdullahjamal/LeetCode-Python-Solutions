class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        count = 0
        
        for i in range(1,len(nums)):
            if nums[i]!= nums[count]:
                count+=1
                nums[count] = nums[i]
                
        return count + 1

        '''
        if len(nums) < 1:
            return len(nums)
        
        i = 1
        
        while (i < len(nums)):
            
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i+=1
                
        return len(nums)
        '''
