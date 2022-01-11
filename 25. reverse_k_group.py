class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    count = 0
    pointer = head
    while pointer is not None and count < k:
        
    pass


head = [1,2,3,4,5]
print(reverse_k_group(head, 2))
print(reverse_k_group(head, 3))
