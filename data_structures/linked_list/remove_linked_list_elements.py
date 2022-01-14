'''
    Leetcode - Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = ListNode()
        while current:
            if current.val == val:
                current = current.next
                prev.next = current

                if head.val == val:
                    head = current
            else:
                prev = current
                current = current.next

        return head
