def inorder_traversal(node):
    t_stack = [node]
    while(len(t_stack) > 0):
        node = t_stack.pop()
        if node:
            while (node.left is not None and not node.left.visited):
                t_stack.append(node)
                node = node.left
            if node.right:
                t_stack.append(node.right)
        node.visited = True
        yield node
