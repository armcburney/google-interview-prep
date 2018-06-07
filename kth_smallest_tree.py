# Similar to the BST iterator problem


class Solution:
    def kthSmallest(self, root, k):
        self.traversed_stack = []
        self.push_stack(root)

        for i in range(k - 1):
            self.next()

        return self.next()

    def next(self):
        node = self.traversed_stack.pop()

        if node.right is not None:
            self.push_stack(node.right)

        return node.val

    def push_stack(self, node):
        if node is None:
            return
        else:
            self.traversed_stack.append(node)
            self.push_stack(node.left)
