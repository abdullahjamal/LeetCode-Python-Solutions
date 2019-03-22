class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanletters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(0,len(s)):
            
            if s[i+1:i+2] and romanletters[s[i]] < romanletters[s[i+1:i+2]]:
                result -=romanletters[s[i]]
            else:
                result +=romanletters[s[i]]
                
        return result
