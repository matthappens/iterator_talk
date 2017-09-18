import random


class IterableTree(object):

    def __init__(self):
        self.root = None

    def __iter__(self):
        self.clear_visited()
        return InorderTraversalIterator(self.root)

    def insert(self, value):
        z = TreeNode(value)
        parent = None
        traverse = self.root
        while traverse:
            parent = traverse
            if z.value < traverse.value:
                traverse = traverse.left
            else:
                traverse = traverse.right
        z.parent = parent
        if parent is None:
            self.root = z
        elif z.value < parent.value:
            parent.left = z
        else:
            parent.right = z

    def inorder_traversal(self, node):
        def it(node):
            if node:
                it(node.left)
                print node.value
                it(node.right)
        it(self.root)

    def clear_visited(self):
        """ Use this to reset the tree between iterations
        """
        def unvisit(n):
            if n:
                n.visited = False
                unvisit(n.left)
                unvisit(n.right)
        unvisit(self.root)


class InorderTraversalIterator(object):

    def __init__(self, root):
        self.root = root
        self.t_stack = [self.root]

    def next(self):
        if len(self.t_stack) > 0:
            node = self.t_stack.pop()
            while (node.left is not None and not node.left.visited):
                self.t_stack.append(node)
                node = node.left
            if node.right:
                self.t_stack.append(node.right)
            node.visited = True
            return node
        else:
            raise StopIteration()


class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.visited = False

    def __repr__(self):
        return self.value


def make_tree():
    it = IterableTree()
    for i in range(16):
        it.insert(random.randint(0, 16))
    return it


def inorder_traversal(tree):
    def _inorder(node):
        if node:
            _inorder(node.left)
            print(node.value)
            _inorder(node.right)
    _inorder(tree.root)
