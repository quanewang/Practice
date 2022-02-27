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


def validate(node, context):  # in order traversal
    if node is None:
        return

    validate(node.left, context)

    if not context.first and (context.previous and context.previous.val >= node.val):
        context.first = context.previous

    if context.first and (context.previous and node.val < context.previous.val):
        context.second = node

    context.previous = node
    validate(node.right, context)


def top_down_recover(root):
    if root is None:
        return False

    l_max = find_node(root.left, max, root)

    r_min = find_node(root.right, min, root)

    if l_max.val > r_min.val:
        temp = l_max.val
        l_max.val = r_min.val
        r_min.val = temp
        return True

    if root.val < l_max.val:
        temp = root.val
        root.val = l_max.val
        l_max.val = temp
        return True

    if root.val > r_min.val:
        temp = root.val
        root.val = r_min.val
        r_min.val = temp
        return True

    if top_down_recover(root.left):
        return True
    if top_down_recover(root.right):
        return True

    return False


def find_node(root, function, node=None):
    if root is None:
        return node

    if function(node.val, root.val) == root.val:
        node = root

    node = find_node(root.left, function, node)
    node = find_node(root.right, function, node)

    return node





