# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: x = -101
# Output: false
 
# Constraints:
# -231 <= x <= 231 - 1
 
# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        splited = []

        k = x
        count = 0

        while k > 0:
            splited.append(k % 10)
            k = k // 10
            count += 1
        
        result = 0

        for i in splited:
            result += i * pow(10, count - 1)
            count -= 1
        
        return result == x

Solution().isPalindrome(113311)