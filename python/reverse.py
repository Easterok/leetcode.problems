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
        hight_boundary = pow(2, 31)
        low_boundary = -(hight_boundary - 1)

        if x >= 0:
            reversed_x = int(str(x)[::-1])

            return 0 if reversed_x > hight_boundary else reversed_x
        else:
            reversed_x = -int(str(x)[::-1][:-1])

            return 0 if reversed_x < low_boundary else reversed_x

Solution().reverse(0)