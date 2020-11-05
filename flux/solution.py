class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def get_parent(self, node, value, parent):
        if node is None:
            return

        if node.value == value:
            return parent
        else:
            p_l = self.get_parent(node.left, value, node.value)
            p_r = self.get_parent(node.right, value, node.value)
            return p_l if p_l is not None else p_r


def make_tree(numbers):
    if len(numbers) == 0:
        return None

    mid_idx = len(numbers) // 2
    root = Node(numbers[mid_idx])
    root.left = make_tree(numbers[:mid_idx])
    root.right = make_tree(numbers[mid_idx+1:])
    return root


count = 1
def label_tree(tree):
    if tree is None:
        return

    label_tree(tree.left)
    label_tree(tree.right)

    global count
    tree.value = count
    count += 1

def solution(h, q):
    max_num = 2 ** h - 1
    elements = [x for x in range(1, max_num + 1)]
    tree = make_tree(elements)
    global count
    count = 1
    label_tree(tree)
    ans = []

    for query in q:
        label = tree.get_parent(tree, query, -1)
        if label is None:
            ans.append(-1)
        else:
            ans.append(label)

    return ans

