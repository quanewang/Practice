import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    get_numbers = []
    merged_node = None
    tail = None
    for j in range(len(lists)):
        if lists[j]:
            heapq.heappush(get_numbers, (lists[j].val, j))
    while get_numbers:
        minimum, index = heapq.heappop(get_numbers)
        if merged_node is None:
            merged_node = lists[index]
            tail = merged_node
        else:
            tail.next = lists[index]
            tail = tail.next
        if lists[index] is not None and lists[index].next is not None:
            lists[index] = lists[index].next
            heapq.heappush(get_numbers, (lists[index].val, index))

    return merged_node


first_row = ListNode(1, ListNode(4, ListNode(5)))
second_row = ListNode(1, ListNode(3, ListNode(4)))
third_row = ListNode(2, ListNode(6))
lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
print(merge_k_lists(lists))

first_row = ListNode(1, ListNode(2, ListNode(2)))
second_row = ListNode(1, ListNode(1, ListNode(2)))
lists = [first_row, second_row]
print(merge_k_lists(lists))
