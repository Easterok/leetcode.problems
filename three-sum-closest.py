# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        closest = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]

        def get_distance(candidate):
            return max(target, candidate) - min(target, candidate)

        def is_closest(candidate):
            return get_distance(closest) > get_distance(candidate)

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                candidate = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if candidate == target:
                    return target

                if is_closest(candidate):
                    closest = candidate
                elif candidate < target:
                    l += 1
                else:
                    r -= 1
        
        return closest
