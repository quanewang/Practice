class CustomStack:

    def __init__(self, max_size: int):
        self.stack = []
        self.max_size = max_size
        self.inc_list = dict()

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        top = self.stack.pop(index)
        val = self.inc_list.get(index)
        if val:
            self.inc_list.pop(index)
            self.increment(index, val)
            top += val
        return top

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack) - 1:
            k = len(self.stack)
        k -= 1
        if self.inc_list.get(k) is not None:
            self.inc_list.update({k: val + self.inc_list.get(k)})
        else:
            self.inc_list.update({k: val})
