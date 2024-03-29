# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Example 3:
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]

# Example 4:
# Input: head = [1], k = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        pointer = head

        while pointer:
            temp_next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = temp_next

        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def reverseGroup(node: ListNode) -> ListNode:
            first_pointer = node
            second_pointer = node

            i = 1

            while first_pointer and i < k:
                first_pointer = first_pointer.next
                i += 1

            if first_pointer is None:
                return node

            temp_first_pointer_next = first_pointer.next

            first_pointer.next = None

            new_head = self.reverse(second_pointer)

            if temp_first_pointer_next is None:
                return new_head

            second_pointer.next = reverseGroup(temp_first_pointer_next)

            return new_head

        return reverseGroup(head)