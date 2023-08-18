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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev


def create_linked_list(ls: Optional[list]) -> Optional[ListNode]:
    ls_copy = ls.copy()
    head = ListNode(ls_copy.pop(0)) if ls_copy else None
    cur = head
    while ls_copy:
        cur.next = ListNode(ls_copy.pop(0))
        cur = cur.next
    return head


# ls = [1, 2, 3, 4, 5]
# head = create_linked_list(ls)
# print(head)

# test = Solution()
# res = test.reverseList(head)
# print(res)
