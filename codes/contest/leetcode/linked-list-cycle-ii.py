#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        idx = 0
        while head:
            if hasattr(head, 'idx'): return head
            head.idx = idx
            idx += 1
            head = head.next
        return None
