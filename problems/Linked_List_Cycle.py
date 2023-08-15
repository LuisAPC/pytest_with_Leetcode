from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2 POINTERS SOLUTION
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# HASHSET SOLUTION
# nodeSet = set()
# while head:
#     if head in nodeSet:
#         return True

#     nodeSet.add(head)
#     head = head.next

# return False


def create_linked_list(
    ls: Optional[list], cycle_to_node_idx: int
) -> Optional[ListNode]:
    ls_copy = ls.copy()
    head = ListNode(ls_copy.pop(0)) if ls_copy else None
    cur = head
    cycle_node = None

    if cycle_to_node_idx == 0:
        cycle_node = cur

    while ls_copy:
        cur.next = ListNode(ls_copy.pop(0))
        cur = cur.next
        cycle_to_node_idx -= 1

        if cycle_to_node_idx == 0:
            cycle_node = cur

    if cycle_node:
        cur.next = cycle_node

    return head


# head = create_linked_list([3, 2, 0, -4], 1)
# test = Solution()
# print(test.hasCycle(head))
