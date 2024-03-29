# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return ""

        press_on = list(map(lambda x: buttons.get(x), list(digits)))

        def combine(arr):
            if len(arr) == 1 or len(arr[1]) == 0:
                return arr[0]

            result = []

            for i in arr[0]:
                for k in arr[1]:
                    result.append(i + k)

            return combine([result] + arr[2:])

        return combine(press_on)
            
Solution().letterCombinations("234")