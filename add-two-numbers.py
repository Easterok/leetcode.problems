# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return "{}".format(self.val)

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0)

            if (l1 and l1.next) or (l2 and l2.next):
                return ListNode(val, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None))
            else:
                return ListNode(val, None)

        else:
            return None


res = Solution().addTwoNumbers(ListNode(1, ListNode(2, None)), ListNode(2, None))

cur = res
while cur:
    print(cur)
    cur = cur.next
