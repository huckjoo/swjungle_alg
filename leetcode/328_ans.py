class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        odd = head
        even = head.next  # None이라도 상관없음, while문 안도니까
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            # 2개씩 2칸씩 움직임..예술
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head
