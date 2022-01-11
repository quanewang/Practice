import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    merged_numbers = []
    get_numbers = []

    for j in range(len(lists)):
        if lists[j]:
            get_numbers.append((lists[j].val, j))
    while get_numbers:
        minimum, index = min(get_numbers)
        get_numbers.remove((minimum, index))
        merged_numbers.append(minimum)
        if lists[index] is not None and lists[index].next is not None:
            lists[index] = lists[index].next
            get_numbers.append((lists[index].val, index))

    if merged_numbers:
        merged_node = ListNode(merged_numbers[0])
        copy = merged_node
        for i in range(1, len(merged_numbers)):
            copy.next = ListNode(merged_numbers[i])
            copy = copy.next
        return merged_node
    return None


first_row = ListNode(1, ListNode(4, ListNode(5)))
second_row = ListNode(1, ListNode(3, ListNode(4)))
third_row = ListNode(2, ListNode(6))
lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
print(merge_k_lists(lists))
