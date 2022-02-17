class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root):
    validate(root, [])


def validate(node, previous_nodes):
    for i in range(len(previous_nodes)):
        parent, subtree = previous_nodes[i]
        if subtree == 0:
            if parent.val < node.val:  # swap
                temp = parent.val
                parent.val = node.val
                node.val = temp

                return True

        else:
            if parent.val > node.val:  # swap
                temp = parent.val
                parent.val = node.val
                node.val = temp

                return True
        
    copy = previous_nodes.copy()
    if node.left:
        copy.append((node, 0))
        if validate(node.left, copy):
            return True

    copy = previous_nodes.copy()
    if node.right:
        copy.append((node, 1))
        if validate(node.right, copy):
            return True



    return False



