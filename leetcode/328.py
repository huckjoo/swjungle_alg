from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0개,1개,2개
        if head == None or head.next == None or head.next.next == None:
            return head
        # 3개
        if head.next.next.next == None:
            cur = head
            nxt = cur.next
            tail = nxt.next
            cur.next = tail
            nxt.next = None
            tail.next = nxt
            return cur

        # 4개부터
        odd_head = head
        even_head = head.next
        flag = 1  # odd
        cur = head
        last_even_node = head
        while (cur.next != None) and (cur.next.next != None):
            nxt = cur.next

            if flag == 1:  # 현재 odd
                last_odd_node = cur.next.next
                flag = 2  # 다음노드 even
            else:         # 현재 even
                flag = 1  # 다음노드 odd
                last_even_node = cur.next.next

            cur.next = nxt.next
            cur = nxt

        last_even_node.next = None  # 3개이상
        last_odd_node.next = even_head
        return odd_head
