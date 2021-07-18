from random import shuffle
import math
import random

def split_data(data):
    train = []
    test = []
    random.shuffle(data)
    train_ele = math.ceil(len(data) * 0.7)
    for i in range(train_ele):
        train.append(data.pop())
    test = data
    return train, test

if __name__ =='__main__':
    data = [{"name": "kartik", "out" : 1}, {"name": "annu", 'out': 2}]
    data = [{"name": "kartik", "out" : 1}]
    data = [
        {"name": "kartik", "out" : 1}, {"name": "annu", 'out': 2}, {"name": "lol", 'out': 3}, 
        {"name": "lol2", 'out': 4}
    ]
    print('hello')
    split_data(data)