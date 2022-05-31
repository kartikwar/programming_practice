"""hash map or hash table is a data structure, 
that implements a hash function to decrease 
the time complexity of accessing an element 
O(1) in general, in python dicts are the 
in built hash map and we dont need to implement
this. This file just gives an insight into how
hash maps work."""

class HashMap():
    def __init__(self):
        MAX_LENGTH = 100
        self.values = [None]*MAX_LENGTH
        self.MAX_LENGTH = MAX_LENGTH

    def get_hash(self, key):
        assert type(key) is str, "only strings supported in keys"
        sum_charcs = 0
        for charc in key:
            #add askii value of character
            sum_charcs += ord(charc)
        index = sum_charcs % self.MAX_LENGTH
        return index

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.values[index] = value

    def __getitem__(self, key):
        index = self.get_hash(key)
        assert self.values[index] != None, "key not found"
        return self.values[index]

    def __delitem__(self, key):
        index = self.get_hash(key)
        assert(self.values[index] != None)
        self.values[index] = None

    def __str__(self):
        return "%a"%self.values 


if __name__ == '__main__':
    hash_map = HashMap()
    hash_map['lol'] = 12
    # hash_map[12] = 123
    print(hash_map)
    print(hash_map['lol'])
    # print(hash_map['bro'])
    del(hash_map['lol'])
    print(hash_map)
        


