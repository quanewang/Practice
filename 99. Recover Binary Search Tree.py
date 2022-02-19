class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Context:
    def __init__(self, previous=None, first=None, second=None):
        self.first = first
        self.second = second
        self.previous = previous


def recoverTree(root):
    context = Context()
    validate(root, context)

    first = context.first
    second = context.second

    if not first or not second:
        return

    temp = first.val
    first.val = second.val
    second.val = temp


def validate(node, context): # in order traversal
    if node is None:
        return

    validate(node.left, context)

    if not context.first and (context.previous and context.previous.val >= node.val):
        context.first = context.previous

    if context.first and (context.previous and node.val < context.previous.val):
        context.second = node

    context.previous = node
    validate(node.right, context)







