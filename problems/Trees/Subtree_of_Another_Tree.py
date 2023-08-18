from typing import Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.val if node else None, self.__node_iter()))

    def __node_iter(self):
        root = self

        q = [root]
        while q:
            validLevel = False
            level = []

            for i in range(len(q)):
                node = q.pop(0)
                level.append(node)

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    validLevel = True

            if validLevel:
                for node in level:
                    yield node


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)


def create_Binary_Tree(elements: Optional[list]) -> Optional[TreeNode]:
    if not elements:
        return None
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, val in enumerate(elements[1:]):
        if val is None:
            continue
        parent_node = nodes[i // 2]
        is_left = i % 2 == 0
        node = TreeNode(val=val)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


# tree = create_Binary_Tree(elements=[4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7])
tree1 = create_Binary_Tree(elements=[3, 4, 5, 1, 2])
tree2 = create_Binary_Tree(elements=[4, 1, 2])
# print(tree)

test = Solution()
res = test.isSubtree(tree1, tree2)
print(res)
