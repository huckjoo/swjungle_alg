from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 단계별로 하나씩 풀고 그 단계를 끝내면 다음 node로 옮기면 됨. 한번에 모든 단계를 생각할 필요 없음


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            prev.next = b
            a.next = b.next
            b.next = a
            prev = a
        return dummy.next
