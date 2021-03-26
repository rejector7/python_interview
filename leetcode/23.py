# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
from queue import PriorityQueue

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         list_num = len(lists)
#         root = ListNode()
#         cur = root
#         heads_heap = []
#         global_index = 0
#         # heapq.heapify(heads_heap)
#         if list_num == 0:
#             return root.next
#         for i in range(list_num):
#             if lists[i] is not None:
#                 heapq.heappush(heads_heap, (lists[i].val, global_index, lists[i]))
#                 global_index += 1
#         while len(heads_heap) > 0:
#             min_node = heapq.heappop(heads_heap)[2]
#             cur.next = min_node
#             cur = cur.next
#             if min_node.next is not None:
#                 heapq.heappush(heads_heap, (min_node.next.val, global_index, min_node.next))
#                 global_index += 1
#         return root.next



# ListNode.__lt__ = lambda self, y: self.val <= y.val
#
#
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         head = point = ListNode(0)
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put((l.val, l))
#         while not q.empty():
#             val, node = q.get()
#             point.next = ListNode(val)
#             point = point.next
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return head.next

from collections import deque
class Solution():
    def mergeKLists(self, lists):
        def mergeTwoLists(list1, list2):
            root = ListNode()
            cur = root
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
            if list1:
                cur.next = list1
            if list2:
                cur.next = list2
            return root.next
        if len(lists) == 0:
            return None
        queue = deque(lists)
        while len(queue) > 1:
            for i in range(len(queue)//2):
                temp_list1 = queue.popleft()
                temp_list2 = queue.popleft()
                queue.append(mergeTwoLists(temp_list1, temp_list2))
        return queue[0]

