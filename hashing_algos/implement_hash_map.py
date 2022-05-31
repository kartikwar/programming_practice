"""hash map or hash table is a data structure, 
that implements a hash function to decrease 
the time complexity of accessing an element 
O(1) in general, in python dicts are the 
in built hash map and we dont need to implement
this. This file just gives an insight into how
hash maps work.
Note that this also implements collision i.e. if two 
keys have same hash index, it stores both of them
"""

class HashMap():
    def __init__(self):
        MAX_LENGTH = 10
        self.values = [[] for i in range(MAX_LENGTH)]
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
        found = False
        for i, ele in enumerate(self.values[index]):
            if ele[0] == key:
               self.values[index][i] = (key, value)
               found = True
               break
        if not found:
            self.values[index].append((key,value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        found = False
        for i, ele in enumerate(self.values[index]):
            if ele[0] == key:
            #    self.values[index][i] = (key, value)
               found = True
               return ele[1]
        assert found == False, "key not found"
        # return ele[1]

    def __delitem__(self, key):
        index = self.get_hash(key)
        for i, ele in enumerate(self.values[index]):
            if ele[0] == key:
               del self.values[index][i]
        # assert(self.values[index] != None)
        # self.values[index] = None

    def __str__(self):
        return "%a"%self.values 


if __name__ == '__main__':
    hash_map = HashMap()
    print(hash_map.get_hash('march 6'))
    hash_map['march 6'] = 6
    # hash_map[12] = 123
    print(hash_map)
    hash_map['march 17'] = 17
    print(hash_map['march 6'])
    print(hash_map['march 17'])
    hash_map['march 17'] = 34
    print(hash_map)
    # print(hash_map['bro'])
    del(hash_map['lol'])
    del(hash_map['march 17'])
    print(hash_map)
        


