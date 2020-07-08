class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, node, new_val):
        if new_val < node.value:
            if not node.left:
                node.left = Node(new_val)
            else:
                self.insert_helper(node.left, new_val)
        elif new_val > node.value:
            if not node.right:
                node.right = Node(new_val)
            else:
                self.insert_helper(node.right, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, node, find_val):
        if node.value == find_val:
            return True
        else:
            if find_val < node.value and node.left:
                self.search_helper(node.left, find_val)
            elif find_val > find_val and node.right:
                self.search_helper(node.right, find_val)
            else:
                return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))