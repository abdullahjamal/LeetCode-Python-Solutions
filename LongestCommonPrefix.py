import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        for i in range(0,len(strs[0])):
            
            for string in strs[1:]:
                if i >=len(string) or string[i] != strs[0][i] :
                    return strs[0][:i]
                
        return strs[0]
        
        #return os.path.commonprefix(strs)
