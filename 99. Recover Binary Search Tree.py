class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def recoverTree(root):
    validate(root)


def validate(node, previous_nodes = None):
    if node.left:
        previous_nodes.append((node, 0))
        validate(node.left, previous_nodes)

    if node.right:
        previous_nodes.append((node, 1))
        validate(node.right, previous_nodes)

    for parent, subtree in previous_nodes:
        if subtree == 0:
            if parent.val > node.val:
                pass  # swap

        else:
            if parent.val < node.val:
                pass  # swap


