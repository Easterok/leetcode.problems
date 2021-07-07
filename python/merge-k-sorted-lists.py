# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []
 

# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

# time issues
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        filtered_lists = list(filter(lambda x: not x is None, lists))

        def fn(list):
            if len(list) == 0:
                return None

            if len(list) == 1:
                return list[0]

            def min_value_node(nodes: List[ListNode]) -> int:
                elem = 0

                for index in range(1, len(nodes)):
                    val = nodes[index].val

                    if val < nodes[elem].val:
                        elem = index
                
                return elem
            
            min_value_index = min_value_node(list)
            min_elem = list[min_value_index]

            if min_elem.next is None:
                list.pop(min_value_index)
            else:
                list[min_value_index] = list[min_value_index].next

            min_elem.next = self.mergeKLists(list)

            return min_elem
        
        return fn(filtered_lists)

Solution().mergeKLists(
    [
        ListNode(2), None, ListNode(1)
    ]
)
