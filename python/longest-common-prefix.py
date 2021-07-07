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

# recursive solution
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         def rec(index) -> str:
#             rec_res = True

#             if len(strs[0]) == index:
#                 return ""

#             for str in range(1, len(strs)):
#                 if len(strs[str]) == index:
#                     return ""
                
#                 rec_res = rec_res and strs[str][index] == strs[0][index]

#             if rec_res:
#                 return strs[0][index] + rec(index + 1)
#             else:
#                 return ""

#         return rec(0)

# binary search solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 200

        for str in strs:
            min_length = min(min_length, len(str))
        
        low = 1
        hight = min_length
        
        def is_common_prefix(middle: int) -> bool:
            str1 = strs[0][:middle]

            for i in range(1, len(strs)):
                if not strs[i].startswith(str1):
                    return False
            
            return True

        while low <= hight:
            middle = (hight + low) // 2

            if is_common_prefix(middle):
                low = middle + 1
            else:
                hight = middle - 1
        
        return strs[0][:(low + hight) // 2]