class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        usedchar = {}
        maxlen = 0
        strt = 0
        for i,c in enumerate(s):
            if c in usedchar and strt<=usedchar[c]:
                strt = usedchar[c] + 1
            else:
                maxlen = max(maxlen, i-strt+1)
                
            usedchar[c] = i
            
        return maxlen
