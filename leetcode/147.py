# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):

        dummy = cur = ListNode(0)

        while head:
            # 삽입할 자리 찾기
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # insertion 실행
            head.next, cur.next, head = cur.next, head, head.next

            # 이 head는 지금 insertion을 수행하지 않은 head이다.
            if head and cur.val > head.val:
                cur = dummy  # 처음으로 돌아감

        return dummy.next
