# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        if (x > y):
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = x

        while start <= end:
            partX = (start + end) // 2
            partY = (x + y + 1) // 2 - partX

            maxLeftX = float('-inf') if partX == 0 else nums1[partX - 1]
            minRightX = float('inf') if partX == x else nums1[partX]

            maxLeftY = float('-inf') if partY == 0 else nums2[partY - 1]
            minRightY = float('inf') if partY == y else nums2[partY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            elif maxLeftX > minRightY:
                end = partX - 1

            else:
                start = partX + 1

Solution().findMedianSortedArrays([1, 2], [3, 4])
