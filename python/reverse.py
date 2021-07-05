# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

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

# Example 4:
# Input: x = 0
# Output: 0
 
# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        low_boundary = -0x80000000
        hight_boundary = 0x7fffffff

        if x > 0:
            reversed_x = int(str(x)[::-1])

            return reversed_x if reversed_x & hight_boundary != hight_boundary else 0
        else:
            reversed_x = -int(str(x)[::-1][:-1])

            return reversed_x if reversed_x & low_boundary != low_boundary else 0
