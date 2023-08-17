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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def heightOfBinaryTree(root):
            if not root:
                return 0

            left = heightOfBinaryTree(root.left)
            right = heightOfBinaryTree(root.right)

            height = 1 + max(left, right)
            diameter[0] = max(left+right, diameter[0])

            return height

        heightOfBinaryTree(root)
        return diameter[0]


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
# tree = create_Binary_Tree(elements=[3, 9, 20, None, None, 15, 7])
tree = create_Binary_Tree(elements=[])
print(tree)

test = Solution()
res = test.diameterOfBinaryTree(tree)
print(res)
