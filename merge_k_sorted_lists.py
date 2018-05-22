"""
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
"""


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
        if len(lists) is 0:
            return None

        head = None

        for l in lists:
            if head is None:
                head = l
            else:
                head = self.merge(head, l)

        return head

    def merge(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        curr_node, head_node = None, None

        while 1:
            if list1 is None and list2 is None:
                break
            elif list1 is not None and (list2 is None or list1.val <= list2.val):
                next_node = ListNode(list1.val)
                list1 = list1.next
            else:
                next_node = ListNode(list2.val)
                list2 = list2.next

            if curr_node is not None:
                curr_node.next = next_node
            else:
                head_node = next_node

            curr_node = next_node

        return head_node
