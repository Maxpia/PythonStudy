# random.py
import random

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number
    
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(data)
    while data: print(random_pop(data))
    print(data)
    data = [1, 2, 3, 4, 5]
    print(data)
    while data: print(random_pop2(data))
    print(data)
    data = [1, 2, 3, 4, 5]
    print(data)
    random.shuffle(data)
    print(data)
    random.shuffle(data)
    print(data)