class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    second = head.next
    temp = second.next
    second.next = head
    head.next = swap_pairs(temp)
    return second


print(swap_pairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
print(swap_pairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
print(swap_pairs(ListNode(1)))
print(swap_pairs(ListNode(1, ListNode(2))))
print(swap_pairs(ListNode(1, ListNode(2, ListNode(3)))))
