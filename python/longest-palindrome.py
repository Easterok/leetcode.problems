# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        def is_palindrome(str: str) -> bool:
            return str == str[::-1]

        for i in range(len(s) + 1):
            for k in range(i + 1, len(s) + 1):
                substr = s[i:k]

                result = substr if is_palindrome(substr) and len(substr) > len(result) else result

        return result

