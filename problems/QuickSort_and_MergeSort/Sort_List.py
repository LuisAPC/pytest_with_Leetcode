# Sort Colors, Kth Largest Element in an array

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.val, self.__node_iter()))

    def __node_iter(self):
        node = self
        while node:
            yield node
            node = node.next


class Solution:
    # merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        # find middle and split in two halfs
        left = head
        right = self.getMid(head)

        # recursion
        left = self.sortList(left)
        right = self.sortList(right)

        # merge in correct order
        return self.merge(left, right)

    def getMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        return mid

    def merge(self, left, right):
        dummy = ListNode()
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next


def create_linked_list(ls: Optional[list]) -> Optional[ListNode]:
    ls_copy = ls.copy()
    head = ListNode(ls_copy.pop(0)) if ls_copy else None
    cur = head
    while ls_copy:
        cur.next = ListNode(ls_copy.pop(0))
        cur = cur.next
    return head


ls = [4, 2, 1, 3]
head = create_linked_list(ls)
print(head)

test = Solution()
res = test.sortList(head)
print(res)
