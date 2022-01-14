'''
    Leetcode - Remove Duplicates from Sorted List: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = ListNode()
        while current:
            if current.val == prev.val:
                current = current.next
                prev.next = current

                if head.val == prev.val:
                    head = prev
            else:
                prev = current
                current = current.next

        return head
