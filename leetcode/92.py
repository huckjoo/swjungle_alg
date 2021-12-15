from collections import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        point = dummy
        cnt = 0
        if head == None or head.next == None or left == right:
            return head
        while point:
            if cnt == left - 1:
                main_head = point
            if cnt == left:  # reverse 시작
                cur = point
                reverse_head = cur
                prev = None
                while cur and cnt <= right:
                    temp = cur
                    cur = cur.next
                    temp.next = prev
                    prev = temp
                    cnt += 1
                reverse_head.next = cur
                main_head.next = prev
                return dummy.next
            point = point.next
            cnt += 1
