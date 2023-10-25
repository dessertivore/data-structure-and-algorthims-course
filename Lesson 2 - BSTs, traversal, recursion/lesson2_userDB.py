"""
Q1: as a senior backend engineer, you are tasked
with developing a fast in-memory data
structure to manage profile info (username
name and email) for 100million users.
1. Insert profile information
2. Find profile info of a user, given username
3. update profile information of a user, given their username
4. list all users of platform, sorted by username
Assume all usernames are unique.
"""

from lesson2 import tree_size, display_keys, User, user_dataset_2
from lesson2_BST import find, insert, fix_unbalanced_BST, update, list_all


class TreeMap:
    def __init__(self):
        self.root = None

    # insert and update
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, value)
            self.root = fix_unbalanced_BST(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)


# populate a new database with some users from previous list
treemap = TreeMap()
(
    treemap["john"],
    treemap["jane"],
    treemap["captainjl"],
    treemap["kathrynj"],
    treemap["chrisp"],
    treemap["scotc"],
) = user_dataset_2[0:6]
treemap.display()
