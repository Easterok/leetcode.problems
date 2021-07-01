# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            def fn(_l1: ListNode, _l2: ListNode, _carry: int = 0) -> ListNode:
                if _l1 or _l2:
                    val = (_l1.val if l1 else 0) + (_l2.val if _l2 else 0) + _carry
                    carry = val // 10
                    rest = val % 10

                    if (_l1 and _l1.next) or (_l2 and _l2.next):
                        return ListNode(rest, fn(_l1.next if _l1 else None, _l2.next if _l2 else None, carry))
                    else:
                        return ListNode(rest, None)

                else:
                    return None
            
            return fn(l1, l2)


res = Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3, None))), ListNode(5, ListNode(6, ListNode(4, None))))

cur = res
while cur:
    print(cur.val)
    cur = cur.next
