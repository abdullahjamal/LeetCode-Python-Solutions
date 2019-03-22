class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.list_ind = []
        self.binarysearch(nums,target,0,len(nums)-1)
        if len(self.list_ind) == 0:
            return [-1,-1]
        else:
            return [min(self.list_ind),max(self.list_ind)]
    def binarysearch(self,nums,target,low,high):
    
        if low <=high:
            mid = int( low + high ) / 2
            if target == nums[mid]:
                self.list_ind += [mid]
                self.binarysearch(nums,target,low, mid-1) 
                self.binarysearch(nums,target,mid+1,high)
            elif target < nums[mid]:
                self.binarysearch(nums,target,low,mid-1)
            else:
                self.binarysearch(nums,target,mid+1,high)
