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

# define User
class User:
    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email
        print('User',self.username,'created!')
    
    # define a method: introduce_yourself, which is a function which
    # can act on class
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User: username = {}, name = {}, email = {}.".format(self.username, self.name, self.email)
    
    def __str__(self) -> str:
        return self.__repr__()
    
john = User('john', 'johndoe', 'john@test.com')
jane = User('jane', 'jane doe', 'jane@doe.com')
captainjl = User('captainjl', 'jean luc picard', 'jeanluc@picard.enterprise')
kathrynj = User('kathrynj', 'captain kathryn janeway', 'kathryn@janeway.voyager')
chrisp = User('chrisp', 'chris pike', 'chris@pike.enterprise')

testusersdataset = [john, jane, captainjl, kathrynj]

# these 2 lines do the same thing
john.introduce_yourself('dave')
User.introduce_yourself(john, 'dave')

# this uses the 'represent' function. Repr and str do similar things
# but str uses the repr method
print(john)

class UserDatabase:
    #initialise, with option to add initial user list
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
        #check that email doesn't exist and raise error if it does
        try:
            self.find_by_email(user.email)
        except ValueError:
            email_error = True
        else:
            raise ValueError("This email is already assigned to a username.")
        if username_error and email_error:
            i = 0
            while i < len(self.users):
                #find first username greater than the user's
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

test_database.update(User(username='john', name='john doe', email='jonnyboy@doe.com'))
#find email and print result user
print(test_database.find_by_email('jane@doe.com'))
# try to find user that doesn't exist- update function returns same error
# print(test_database.find_by_username('dessertivore'))
# print all
print(test_database.list_all())