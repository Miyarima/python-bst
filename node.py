"""
This is a module containing the Node class
"""
class Node:
    """ The Node class """
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self):
        """ Returns False if the left child is none """
        return self.left is not None

    def has_right_child(self):
        """ Returns False if the right child is none """
        return self.right is not None

    def has_both_children(self):
        """ Returns False if either left or right child is none """
        return self.left is not None and self.right is not None

    def has_parent(self):
        """ Returns False if node has no parent """
        return self.parent is not None

    def is_left_child(self):
        """ Returns False if node isn't left child """
        if self.parent.left is None:
            return False
        return self.parent.left.key == self.key

    def is_right_child(self):
        """ Returns False if node isn't right child """
        if self.parent.right is None:
            return False
        return self.parent.right.key == self.key

    def is_leaf(self):
        """ Returns False if node isn't leaf """
        return not self.has_left_child() and not self.has_right_child()

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other
