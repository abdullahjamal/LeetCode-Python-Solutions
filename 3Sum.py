class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        rightone = len(nums) - 1
        triplet = []
        
        for i , no in enumerate(nums):
            left = i+1
            right = rightone
            while left < right:
                sum_ = (no + nums[left] + nums[right])

                if sum_ == 0:
                    triplet_found = [no,nums[left],nums[right]]
                    if triplet_found not in triplet:
                        triplet.append(triplet_found)
                    
                    right -=1

                elif sum_ < 0:
                    left +=1
                else:
                    right -=1
        
        return triplet
