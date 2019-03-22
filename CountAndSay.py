class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            return self.count(self.countAndSay(n-1))
        
    def count(self,s):
        c=s[0]
        result = ""
        count = 1
        for char in s[1:]:
            if char == c:
                count+=1
            else:
                result = result + str(count) + c
                c = char
                count=1 
        result = result + str(count) + c
        return result
            
        
        
        
        
        
                
                
            
            
