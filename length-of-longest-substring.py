# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        if len(s) == 0:
            return result

        def isUniq(str: str) -> bool:
            return len(set(str)) == len(str)
        
        for i in range(len(s) + 1):
            for k in range(i + 1, len(s) + 1):
                substr = s[i:k]
                substr_len = len(substr)

                if isUniq(substr):
                    result = result if substr_len < result else substr_len


        return result


def test_answer():
    assert Solution().lengthOfLongestSubstring("qwerty") == 6
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("  qw") == 3
    assert Solution().lengthOfLongestSubstring("q w e r") == 3


test_answer()