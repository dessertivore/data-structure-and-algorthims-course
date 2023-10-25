from lesson2 import User, john, kathrynj, chrisp

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


def parse_tuple_to_tree(data) -> TreeNode | None:
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
tree1 = parse_tuple_to_tree(binary_tree_tuple)
if not tree1:
    raise ValueError
print(tree1.traverse_in_order())

print(check_bst(tree1))

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


"""
Make new class BSTNode with parents as well
"""


# value is optional, but would be e.g. of type User,
# whilst key would be equivalent to username
class BSTNode:
    def __init__(self, key: str, value=None):
        self.key = key
        self.value = value
        self.left: None | BSTNode = None
        self.right: None | BSTNode = None
        self.parent: None | BSTNode = None


# to view level 1 if BSTNode called tree
# print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

"""
QUESTION 11: Write a function to insert a new node 
into a BST.
"""


def insert(node: BSTNode | None, value: User) -> BSTNode:
    if node is None:
        node = BSTNode(value.username, value)
    elif value.username <= node.key:
        node.left = insert(node.left, value)
        node.left.parent = node
    elif value.username > node.key:
        node.right = insert(node.right, value)
        node.right.parent = node
    return node


"""
if tree is unbalanced, time complexity is O(N).
If it is balanced, it will be O(logN)
"""

# initialise tree by adding first instance
# order of insertion will affect tree structure
tree = insert(None, kathrynj)
insert(tree, john)
insert(tree, chrisp)

if not tree.left:
    raise ValueError
if not tree.left.left:
    raise ValueError
print(tree.key, tree.left.left.value)

"""
find a key
"""


def find(node: BSTNode | None, keysearch: str):
    if node is None:
        return None
    if keysearch == node.key:
        return node.value
    if keysearch < node.key:
        return find(node.left, keysearch)
    if keysearch > node.key:
        return find(node.right, keysearch)


# for example print(find(tree, "john"))

# The the length of the path followed by find
# is equal to the height of the tree (in the worst case).
# Thus it has a similar time complexity as insert.

"""
QUESTION 12: Write a function to update the 
value associated with a given key within a BST
"""


def update(BST: BSTNode, key, new_value):
    target = find(BST, key)
    if target is not None:
        target.value = new_value


# see below for example of how to use this to update
# john's name on his file.
# update(tree, john, User('john', 'john coding expert, 'johnnyboy@doe.com'))

"""
QUESTION 13: Write a function to retrieve 
all the key-values pairs stored in a BST in the 
sorted order of keys.
"""


def list_all(node):
    if node is None:
        return []
    # list all on left, list middle, list all on right
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


"""
time and space complexity are both O(N) - 
must list all keys so it must go through all of them.
The space complexity of the list_all function is O(n) 
as well. This is because it uses a recursive approach,
and each recursive call adds a new frame to the call stack. 
In the worst case, where the BST is completely unbalanced
(essentially a linked list), there can be n recursive calls 
on the call stack, leading to O(n) space complexity.
"""

"""
QUESTION 14: Write a function to determine 
if a binary tree is balanced.

"""


def balance_check(tree: BSTNode | None):
    if tree is None:
        # An empty tree is considered balanced
        return True, 0

    # Check the balance of the left and right subtrees
    left_balanced, left_height = balance_check(tree.left)
    right_balanced, right_height = balance_check(tree.right)

    # Calculate the height of the current node
    current_height = max(left_height, right_height) + 1

    # Check if the left and right subtrees are balanced
    is_balanced = (
        left_balanced and right_balanced and abs(left_height - right_height) <= 1
    )

    return is_balanced, current_height


"""
QUESTION 15: Write a function to create a balanced 
BST from a sorted list/array of key-value pairs.
We can use a recursive strategy here, turning the 
middle element of the list into the root, and recursively creating left and right subtrees.
"""


def make_balanced_bst(data: list, lo=0, hi=None, parent=None) -> BSTNode | None:
    if hi is None:
        hi = len(data) - 1
    # make empty subtree if no elements left in sublist
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    # extract data from middle of sublist
    key, value = data[mid]
    # use this data to make a BSTNode
    root = BSTNode(key, value)
    # if this is the middle, parent will be None
    # anywhere else, and previous root is provided as parent
    root.parent = parent
    # lo remains the same, mid changes, to ensure left subtree only uses left of list
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root


"""
QUESTION 16: Write a function to balance an unbalanced binary search tree.
"""


def fix_unbalanced_BST(BSTNode):
    return make_balanced_bst(list_all(BSTNode))


"""
After every insertion, we can balance the tree. This way the tree will remain balanced.

Complexity of the various operations in a balanced BST:

Insert - O(log N) + O(N) = O(N)
Find - O(log N)
Update - O(log N)
List all - O(N)

What's the real improvement between O(N) and O(log N)?

for a list 100000000 long: log(100000000, 2) = 26.5754247590989
The logarithm (base 2) of 100 million is around 26. 
Thus, it takes only 26 operations to find or update a node 
within a BST (as opposed to 100 million).

To speed up insertions, we may choose to perform the balancing periodically 
(e.g. once every 1000 insertions). This way, most insertions will be O (log N), 
but every 1000th insertion will take a few seconds. 
Another options is to rebalance the tree periodically at the end of every hour.
"""
