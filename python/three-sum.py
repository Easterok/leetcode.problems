# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []
 

# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return result
        
        sorted_nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if s == 0:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return result

Solution().threeSum([-1,0,1,2,-1,-4])