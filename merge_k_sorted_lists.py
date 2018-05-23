"""
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
"""

from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = PriorityQueue()

        # Heap sort
        for l in lists:
            node = l
            while node is not None:
                min_heap.put(node.val)
                node = node.next

        head, curr = None, None

        while not min_heap.empty():
            node = ListNode(min_heap.get())

            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node

        return head
