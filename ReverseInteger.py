# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x * -1)[::-1]) * -1
                                                    
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
                                                                            
        if ans > ma or ans < mi:
            return 0
        return ans