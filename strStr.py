class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack.find(needle) == -1:
            return -1
        
        else:
            return haystack.index(needle) 
