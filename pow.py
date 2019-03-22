class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return float(1)
        
        sign = (n > 0)
        n = abs(n)
        
        if n % 2 == 0:
            result = self.myPow(x*x, n//2)
        else:
            result = x * self.myPow( x , n - 1) #x*self.myPow(x*x,n//2)
            
        return result if sign else 1 / result
        
        
       
