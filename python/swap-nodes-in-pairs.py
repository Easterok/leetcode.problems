# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]
 

# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        if head.next is None:
            return head

        guy = ListNode()
        guy.next = head

        first_pointer = head.next
        second_pointer = guy

        while not first_pointer is None:
            temp_first = first_pointer.next
            first_pointer.next = second_pointer.next
            temp_second = second_pointer.next
            second_pointer.next.next = temp_first
            second_pointer.next = first_pointer

            if temp_first is None:
                break

            first_pointer = temp_first.next
            second_pointer = temp_second

        return guy.next