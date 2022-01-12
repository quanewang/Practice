class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    if k == 1:
        return head
    n = 0
    current = head
    while current is not None:  # get the length of the linked list
        n += 1
        current = current.next

    reverse_count = n // k
    return recursive_k_reverse(head, k, reverse_count)


def recursive_k_reverse(head, k, m):
    if m == 0:
        return head
    else:
        h, t = reverse_list(head, k)
        next_head = recursive_k_reverse(t.next, k, m - 1)
        t.next = next_head
    return h


def reverse_list(start, k):
    if k == 2:
        head = start
        tail = start.next
        p2 = tail.next
        tail.next = head
        head.next = p2
        return tail, head
    else:
        h, t = reverse_list(start.next, k - 1)
        p2 = t.next
        start.next = p2
        t.next = start
        t = start
    return h, t


head = ListNode(1, ListNode(2, ListNode(3)))
print(reverse_k_group(head, 3))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverse_k_group(head, 2))

print(reverse_k_group(head, 1))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(reverse_k_group(head, 4))

