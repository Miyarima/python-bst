"""
This is a module containing the BinarySearchTree class
"""
from node import Node

class BinarySearchTree:
    """ The BinarySearchTree class """
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """ Inserts value into the binarytree """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    @classmethod
    def _insert(cls, node, key, value):
        if key < node:
            if node.has_left_child():
                cls._insert(node.left, key, value)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                cls._insert(node.right, key, value)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value

    def inorder_traversal_print(self):
        """ Prints all keys in order """
        self._print_nodes(self.root)

    @classmethod
    def _print_nodes(cls, node):
        if node.has_left_child():
            cls._print_nodes(node.left)

        print(node.key)

        if node.has_right_child():
            cls._print_nodes(node.right)

    def get(self, key):
        """ Returns the value which corresponds to the key """
        if self.root is None:
            raise KeyError
        return self._get(self.root, key).value

    @classmethod
    def _get(cls, node, key):
        to_return = Node
        try:
            if key < node:
                to_return = cls._get(node.left, key)
            if key > node:
                to_return = cls._get(node.right, key)
            if key == node.key:
                to_return = node
            return to_return
        except TypeError as error:
            raise KeyError from error

    def remove(self, key):
        """ Removes the node corresponding to the key and returns the value of the removed node """
        if self.root.key is None:
            raise KeyError
        key_node = self._get(self.root, key)
        return self._remove(key_node)

    @classmethod
    def _remove(cls, node):
        removed_value = node.value
        if node.parent is None:
            if not node.has_right_child() and not node.has_left_child():
                node.key = None
                node.value = None
                return removed_value
            if node.has_left_child() and not node.has_right_child():
                cls._has_left_child(node)
                return removed_value
            if node.has_right_child() and not node.has_left_child():
                cls._has_right_child(node)
                return removed_value
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
            node.parent = None
        if node.has_both_children():
            succ = cls._find_succ(node.right)
            cls._has_both_children(node, succ)
            return removed_value
        if node.has_left_child() or node.has_right_child():
            if node.has_left_child():
                cls._has_child(node, node.left)
            if node.has_right_child():
                cls._has_child(node, node.right)
        return removed_value

    @classmethod
    def _find_succ(cls, node):
        if node.has_left_child():
            return cls._find_succ(node.left)
        return node

    @staticmethod
    def _has_left_child(node):
        if node.left.has_both_children():
            node.left.right.parent = node.left.parent
            node.right = node.left.right
            node.left.right = None
            node.left.left.parent = node.left.parent

            node.key = node.left.key
            node.value = node.left.value
            node.left = node.left.left
            node.left.left = None
        else:
            node.left.parent = None
            node.key = node.left.key
            node.value = node.left.value
            node.left = None

    @staticmethod
    def _has_right_child(node):
        if node.right.has_both_children():
            node.right.left.parent = node.right.parent
            node.left = node.right.left
            node.right.left = None
            node.right.right.parent = node.right.parent

            node.key = node.right.key
            node.value = node.right.value
            node.right = node.right.right
            node.right.right = None
        else:
            node.right.parent = None
            node.key = node.right.key
            node.value = node.right.value
            node.right = None

    @staticmethod
    def _has_child(node, node_dir):
        if node.is_left_child():
            node.parent.left = node_dir
        else:
            node.parent.right = node_dir
        node_dir.parent = node.parent
        node_dir = None
        node.parent = None
        return node.value

    @staticmethod
    def _has_both_children(node, succ):
        node.key = succ.key
        node.value = succ.value
        if succ.has_right_child():
            succ.right.parent = succ.parent
            if succ.is_right_child():
                succ.parent.right = succ.right
            else:
                succ.parent.left = succ.right
            succ.right = None
        else:
            if succ.is_right_child():
                succ.parent.right = None
            else:
                succ.parent.left = None
        succ.parent = None
