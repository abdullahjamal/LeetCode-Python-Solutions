class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permute = []
        self.permute_recur(nums,0,len(nums)-1)
        return self.permute
    
    def permute_recur(self,nums,left,right):
        
        if left == right:
            self.permute.append(nums[:]) 
        else:
            for i in range(left,right+1):
                nums[left],nums[i] = nums[i],nums[left]
                self.permute_recur(nums,left+1,right)
                nums[left],nums[i] = nums[i],nums[left]       
        
        
