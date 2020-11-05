class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
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


def make_tree(height):
    # make tree
    max_num = 2 ** height - 1
    elements = [x for x in range(1, max_num + 1)]
    # insert root element
    tree = Node(elements.pop())
    elements.reverse()
    for e in elements:
        tree.insert(e)

    return tree


def solution(h, q):
    # max heap? find correct number,
    # return list of correct labels
    #   aka. number on parent node
    tree = make_tree(h)
    ans = []

    for query in q:
        label = tree.get_parent(tree, query, -1)
        if label is None:
            ans.append(-1)
        else:
            ans.append(label)

    return ans

