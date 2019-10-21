class Solution:
    def factorial(self,n):
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n-1)

print Solution().factorial(5)




"""
    5!                  = 120
    5 * 4!              = 120
        4 * 3!          = 24
            3 * 2!      = 6
                2 * 1!  = 2
                    1!  = 1
"""