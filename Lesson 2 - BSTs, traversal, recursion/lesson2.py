# define class username


# define User
class User:
    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email
        print("User", self.username, "created!")

    # define a method: introduce_yourself, which is a function which
    # can act on class
    def introduce_yourself(self, guest_name):
        print(
            "Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email)
        )

    def __repr__(self):
        return "User: username = {}, name = {}, email = {}.".format(
            self.username, self.name, self.email
        )

    def __str__(self) -> str:
        return self.__repr__()


john = User("john", "john doe", "john@test.com")
jane = User("jane", "jane doe", "jane@doe.com")
captainjl = User("captainjl", "jean luc picard", "jeanluc@picard.enterprise")
kathrynj = User("kathrynj", "captain kathryn janeway", "kathryn@janeway.voyager")
chrisp = User("chrisp", "chris pike", "chris@pike.enterprise")
scotc = User("scotc", "scot chegg", "scot@egg.com")

testusersdataset = [john, jane, captainjl, kathrynj]
user_dataset_2 = [john, jane, captainjl, kathrynj, chrisp, scotc]

# these 2 lines do the same thing
# john.introduce_yourself('dave')
# User.introduce_yourself(john, 'dave')

# this uses the 'represent' function. Repr and str do similar things
# but str uses the repr method
# print(john)


class UserDatabase:
    # initialise, with option to add initial user list
    # leave () when initialising to create blank UserDatabase
    def __init__(self, initialuserlist: list[User] = []) -> None:
        self.users = initialuserlist

    # insert in alphabetical order
    def insert(self, user: User):
        username_error = False
        email_error = False
        # check that username doesn't exist and raise error if it does
        try:
            self.find_by_username(user.username)
        except ValueError:
            username_error = True
        else:
            raise ValueError("This username already exists.")
        # check that email doesn't exist and raise error if it does
        try:
            self.find_by_email(user.email)
        except ValueError:
            email_error = True
        else:
            raise ValueError("This email is already assigned to a username.")
        if username_error and email_error:
            i = 0
            while i < len(self.users):
                # find first username greater than the user's
                if self.users[i].username > user.username:
                    break
                i += 1
            self.users.insert(i, user)

    def find_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        # raise value error if no user exists with that username
        raise ValueError(f"No username {username} exists.")

    def find_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        raise ValueError(f"No user with email {email} exists.")

    def update(self, user: User) -> None:
        # update user, keeping username the same
        target = self.find_by_username(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self) -> list[User]:
        return self.users


test_database = UserDatabase(testusersdataset)
test_database.insert(chrisp)

test_database.update(User(username="john", name="john doe", email="jonnyboy@doe.com"))
# find email and print result user
# print(test_database.find_by_email('jane@doe.com'))

# try to find user that doesn't exist- update function returns same error
# print(test_database.find_by_username('dessertivore'))
# print all
# print(test_database.list_all())


# trying to make a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def parse_tuple(data: tuple | None) -> Node | None:
    # add print(data) here to see the function parse all your tuples
    if data is None:
        node = None
    elif isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        # this is a recursive function!
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    else:
        node = Node(data)
    return node


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# make an example tree with data above
exampletree = parse_tuple(tree_tuple)

# have a look at the different nodes
# this prints the value 2 down and right from the top
if not exampletree:
    raise ValueError
print(exampletree.right.right.value)


# convert tree to tuple
def tree_to_tuple(node: Node | None) -> tuple | None:
    # if it has both left and right nodes
    if node is None:
        return None
    if node.left and node.right:
        return (tree_to_tuple(node.left), node.value, tree_to_tuple(node.right))
    # if it has a left node but not a right node
    elif node.left and not node.right:
        return (tree_to_tuple(node.left), node.value, None)
    # if it has no left node but has a right node
    elif not node.left and node.right:
        return (None, node.value, tree_to_tuple(node.right))
    # if no left or right nodes, then make this value into a tuple on its own- it's a leaf
    elif not node.left and not node.right:
        return (node.value,)
    # add this on just so it doesn't get stuck in a loop hopefully
    else:
        return None


print(tree_to_tuple(exampletree))


"""
Q3: write a function to perform the inorder traversal 
(left tree recursively inorder [visit all left nodes from 
bottom to top], current node,
then right tree recursively inorder [visit all
left nodes first]) of a binary tree
"""


# traverse a tree in order
def traverse_in_order(node) -> list:
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.value] + traverse_in_order(node.right)


"""
Write a function to perform the preorder traversal
(start from the top (visit current node), go down all 
left nodes top to bottom, then go to right side 
and visit all of those top to bottom (starting 
with left branches)) of a binary tree
"""


def traverse_preorder(node):
    # will always stop when it reaches empty node
    if node is None:
        return []

    result = [node.value]
    # go down all left branches
    result += traverse_preorder(node.left)
    # go down all right branches
    result += traverse_preorder(node.right)
    return result


"""
Write a function to perform the postorder
traversal (go to left leaf first,
then go all the way to top of left side,
then go to right leaf and go all the way up
right side, then go to root) of a binary tree
"""


def traverse_postorder(node):
    if node is None:
        return []

    result = []

    result += traverse_postorder(node.left)
    result += traverse_postorder(node.right)

    result.append(node.value)
    return result


"""
Write a function to calculate 
height/depth of binary tree
"""


def heightcalc(node: Node) -> int:
    if not node.left and not node.right:
        return 1

    height_l = 0
    height_r = 0

    if node.left:
        height_l = 1 + heightcalc(node.left)
    if node.right:
        height_r = 1 + heightcalc(node.right)

    return max(height_r, height_l)


# a second option for calculating depth
def height_calc(node: Node) -> int:
    if not node:
        # if it is not a node - no depth
        return 0
    if not node.left and not node.right:
        # base case - node with no children
        return 1
    return 1 + max(height_calc(node.left), height_calc(node.right))


"""
Write a function to count the number
of nodes on a binary tree
"""


def tree_size(node) -> int:
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


# display keys with function below, from tutor
def display_keys(node, space="\t", level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + "∅")
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)
