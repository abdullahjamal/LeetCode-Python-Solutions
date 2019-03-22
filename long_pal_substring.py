class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = ""
        for i in range(0,len(s)):
            even_pal = self.palindromeat(s,i,i+1)
            odd_pal = self.palindromeat(s,i,i)
            longest_palindrome = max(longest_palindrome,even_pal,odd_pal,key=len)
        return longest_palindrome
    
    def palindromeat(self,s,left,right):
        while left>=0 and right < len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
        
       
