# 2130. Maximum Twin Sum of a Linked List
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = [head.val]
        n = head.next
        while n:
            a.append(n.val)
            n = n.next
        m = 0
        for i in range(0, len(a)):
            if i > len(a) / 2 - 1:
                break
            if a[i] + a[len(a) - i - 1] > m:
                m = a[i] + a[len(a) - i - 1]
        return m
