# TLE가 나는데 왜 나는지 살펴보기
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        o_head = dummy
        ptr = head
        while ptr:  # input element 순회
            cur = ptr.val
            o_ptr = o_head
            if o_head.next == None:
                o_head.next = ListNode(cur)
            while o_ptr and o_ptr.next:  # insertion sort 실행
                if o_ptr.next.val > cur:
                    new = ListNode(cur)
                    new.next = o_ptr.next
                    o_ptr.next = new
                o_ptr = o_ptr.next
            ptr = ptr.next
        return dummy.next
