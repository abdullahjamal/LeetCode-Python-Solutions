class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            maxarea = max(maxarea, min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
                
        return maxarea
