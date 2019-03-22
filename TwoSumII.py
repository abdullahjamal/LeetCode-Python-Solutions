class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 1 :
            return [-1, -1]
        
        hare  = 0
        tortise = len(numbers) - 1
        
        while (hare < len(numbers) - 1):
            
            if numbers[hare] + numbers[tortise] == target:
                
                return [hare+1, tortise+1]
            
            elif target > (numbers[hare] + numbers[tortise]):
                
                hare += 1
            elif target < (numbers[hare] + numbers[tortise]):
                
                tortise -=1
                
            
