class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        if str == '':
            return 0
        
        i = 0
        while i < len(str) and str[i].isspace():
            i +=1
        sign = 1
        
        if i < len(str) and str[i] == '-':
            sign = -1
            
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        sum = 0
        while i<len(str) and str[i].isdigit():
            if sum > ((2**31 -1)- int(str[i])) / 10:
                return (2**31)-1 if sign > 0 else (-2**31)
            
            sum = sum * 10 + int(str[i])
            i +=1
            
        return sign  * sum
