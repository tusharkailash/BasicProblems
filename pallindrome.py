class Solution(object):
    def isPalindrome(self,s):
        # Run loop from 0 to len/2
        for i in xrange(0, len(s) / 2):
            #print i                           # 0 ,1 ,2, 3
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


s = "malayalam"
print Solution().isPalindrome(s)

"""
lens(s) = 9

         s[i]    s[len(s)-i-1]
i=0       m         m
i=1       a         a
i=2       l         l
i=3       a         a   
"""