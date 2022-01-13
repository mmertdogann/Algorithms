'''
    Leetcode - Middle of the Linked List: https://leetcode.com/problems/middle-of-the-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Straight solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        size = 0

        while current is not None:
            size += 1
            current = current.next

        current = head
        i = 1
        half = (size // 2) + 1
        while current:
            if i == half:
                return current

            i += 1
            current = current.next


# Fast & Slow Pointers solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
