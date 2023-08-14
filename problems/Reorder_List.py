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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            # get values
            l1 = list1.val
            l2 = list2.val

            # update new list and pointers
            if l1 < l2:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # update cur pointers
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next


def create_linked_list(ls: Optional[list]) -> Optional[ListNode]:
    ls_copy = ls.copy()
    head = ListNode(ls_copy.pop(0)) if ls_copy else None
    cur = head
    while ls_copy:
        cur.next = ListNode(ls_copy.pop(0))
        cur = cur.next
    return head


# ls1 = [1, 2, 4]
# ls2 = [1, 3, 4]
# ll1 = create_linked_list(ls1)
# ll2 = create_linked_list(ls2)
# print(ll1)
# print(ll2)

# test = Solution()
# res = test.mergeTwoLists(ll1, ll2)
# print(res)
