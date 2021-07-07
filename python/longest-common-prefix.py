# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def rec(index) -> str:
            rec_res = True

            if len(strs[0]) == index:
                return ""

            for str in range(1, len(strs)):
                if len(strs[str]) == index:
                    return ""
                
                rec_res = rec_res and strs[str][index] == strs[0][index]

            if rec_res:
                return strs[0][index] + rec(index + 1)
            else:
                return ""

        return rec(0)

Solution().longestCommonPrefix(["flower","flow","flight"])