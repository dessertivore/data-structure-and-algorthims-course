"""
Your objective in this assignment is to implement a HashTable class which supports the following operations:

Insert: Insert a new key-value pair
Find: Find the value associated with a key
Update: Update the value associated with a key
List: List all the keys stored in the hash table

Avoid handling collisions with linear probing - see 
end of doc for updated getindex function which
is a bit tidier
"""


class HashTable:
    # initialise hash table maximum number spaces (default 4096)
    def __init__(self, capacity=4096):
        self.data_list = [None] * capacity

    # get the hash of the key, and store the pair at that index in the data list.
    def insert(self, key: str, value: str):
        idx = get_index(self.data_list, key)
        # check if key is already at this index
        if not self.find(key):
            self.data_list[idx] = (key, value)
        # keep adding 1 until empty index reached
        else:  # Handle collisions using linear probing
            while self.data_list[idx] is not None:
                idx = (idx + 1) % len(self.data_list)
            self.data_list[idx] = (key, value)

    def update(self, key: str, value: str):
        idx = get_index(self.data_list, key)
        # if there is no index associated with key
        # return None
        if not self.data_list[idx]:
            return None
        # else, return key value pair from that index
        # after making sure that key matches key at index
        keyfound = self.data_list[idx][0]
        if keyfound == key:
            self.data_list[idx] = (key, value)

    # find, or return error if does not exist
    def find(self, key):
        idx = get_index(self.data_list, key)
        initial_idx = idx  # Store the initial index to check if we've looped through the entire table
        # keep looping until reaches return statement
        while True:
            # If there is no index associated with key, return None
            if self.data_list[idx] is None:
                return None
            # Otherwise, check if the key matches the key at the current index
            k, v = self.data_list[idx]
            if k == key:
                return v  # Return the value associated with the key
            # If the key doesn't match, it might be due to collision; move to the next index
            idx = (idx + 1) % len(self.data_list)
            # If we've checked all possible indices, return None to avoid an infinite loop
            if idx == initial_idx:
                return None

    # print all keys from key value pairs (i.e. values at index 1 of each pair)
    def list_all(self):
        print([kv[0] for kv in self.data_list if kv is not None])


def get_index(data_list: list, a_string: str) -> int:
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index


"""
a couple of examples of strings which can be hashed to values in this list

example = [None] * 4096

print(get_index(example, "Aakash") == 585)
print(get_index(example, "Don O Leary") == 941)
"""

"""
create example hashtable with length 5

example = HashTable(5)
print(len(example.data_list))
"""

example = HashTable()
example.insert("jimK", "James Tiberius Kirk")
example.insert("jimk", "Jamie Tiberius Kirk")
example.insert("Kjim", "Kirk James Tiberius")
example.insert("nurseC", "Nurse Christine Chapel")
print(example.find("Kjim"))
example.list_all()


"""
To make a function that finds valid index from the 
get go:

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv = None
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0
            
            """


"""
Make a python friendly hash table interface
"""


class HashTableImproved:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        idx = hash(key) % len(self.data_list)
        while True:
            # Get the key-value pair stored at idx
            kv = self.data_list[idx]
            # If it is None, return the index
            if not kv:
                return idx
            # If the stored key matches the given key, return the index
            if kv[0] == key:
                return idx
            # Move to the next index
            idx += 1
            # Go back to the start if you have reached the end of the array
            if idx == len(self):
                idx = 0

    def __getitem__(self, key):
        idx = self.get_valid_index(key)
        initial_idx = idx  # Store the initial index to check if we've looped through the entire table
        # keep looping until reaches return statement
        while True:
            # If there is no index associated with key, return None
            if self.data_list[idx] is None:
                return None
            # Otherwise, check if the key matches the key at the current index
            if self.data_list[idx][0] == key:
                return self.data_list[idx][
                    1
                ]  # Return the value associated with the key
            # If the key doesn't match, it might be due to collision; move to the next index
            idx = (idx + 1) % len(self.data_list)
            # If we've checked all possible indices, return None to avoid an infinite loop
            if idx == initial_idx:
                return None

    def __setitem__(self, key, value):
        # check if key exists
        # if not, create new entry
        if not self[key]:
            self.data_list[self.get_valid_index(key)] = (key, value)
            # if entry exists, replace entry at key's index with new value
        if self[key]:
            idx = self.get_valid_index(key)
            self.data_list[idx] = key, value

    def __iter__(self):
        # to call this, use 'for x in example, print(x)'
        # ignores None values
        filtered_items = [x for x in self.data_list if x is not None]
        return iter(filtered_items)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent

        pairs = [
            indent("{} : {}".format(repr(kv[0]), repr(kv[1])), "  ") for kv in self
        ]
        return "{\n" + "{}".format(",\n".join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)


example1 = HashTableImproved()
example1["jimK"] = "James Tiberius Kirk"
example1["jimk"] = "Jamie Tiberius Kirk"
example1["Kjim"] = "Kirk James Tiberius"
example1["nurseC"] = "Nurse Christine Chapel"
print(example1["Kjim"])
for x in example1:
    print(x)
