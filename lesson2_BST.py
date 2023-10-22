"""
Create TreeNode class to encapsulate all of this-
done by tutor
"""


class TreeNode:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

    def height(self):
        if self is None:
            return 0
        if not self.left and not self.right:
            return 1
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self) -> list:
        if self is None:
            return []
        return (
            TreeNode.traverse_in_order(self.left)
            + [self.value]
            + TreeNode.traverse_in_order(self.right)
        )

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.value
        return TreeNode.to_tuple(self.left), self.value, TreeNode.to_tuple(self.right)

    def __str__(self) -> str:
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self) -> str:
        return "BinaryTree <{}>".format(self.to_tuple())


def parse_tuple_to_tree(data) -> TreeNode:
    # add print(data) here to see the function parse all your tuples
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        # this is a recursive function!
        node.left = parse_tuple_to_tree(data[0])
        node.right = parse_tuple_to_tree(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


"""
extra exercises:
maximum depth, minimum depth, diameter of tree
"""


"""
Q8: write a function to check if a binary tree
is a binary search tree (left subtree only contains
nodes with keys less than node's key, and right subtree
only contains nodes with keys greater than node's key)
"""


def check_bst(node: TreeNode) -> bool:
    nodes = node.traverse_in_order()
    for i in range(len(nodes) - 1):
        if nodes[i] > nodes[i + 1]:
            return False
    else:
        return True


# random binary tree tuple
binary_tree_tuple = ((1, 3, (4, 6, 7)), 8, (None, 10, ((13), 14, (None))))

# make this tree into a TreeNode class, then print in order
# to check what this output is like
Tree1 = parse_tuple_to_tree(binary_tree_tuple)
print(Tree1.traverse_in_order())

print(check_bst(Tree1))

"""
Find maximum and minimum keys in a binary tree
"""


def find_min_max(node: TreeNode):
    if node is None:
        return None, None

    min_l, max_l = find_min_max(node.left)
    min_r, max_r = find_min_max(node.right)

    min_list = [min_l, node.value, min_r]
    max_list = [max_l, node.value, max_r]

    # use list comprehension to filter out non-ints
    min_key = min([i for i in min_list if isinstance(i, int)])
    max_key = max([i for i in max_list if isinstance(i, int)])

    return min_key, max_key


print(find_min_max(Tree1))
